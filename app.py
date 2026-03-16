from flask import Flask, request, redirect, url_for, render_template, session, flash
from datetime import datetime
import data_manager

app = Flask(__name__)
app.secret_key = "fundibots-electronics-cms-2025"

# Student progress tracking
student_progress = {}

def get_student_progress(student_id="demo"):
    """Get or initialize student progress"""
    if student_id not in student_progress:
        student_progress[student_id] = {
            "current_index": 0,
            "completed": []
        }
    return student_progress[student_id]

def get_next_credential_id(current_id):
    """Get the next credential ID in sequence"""
    credentials = data_manager.get_all_credentials()
    current_idx = next((i for i, c in enumerate(credentials) if c["id"] == current_id), None)
    if current_idx is not None and current_idx + 1 < len(credentials):
        return credentials[current_idx + 1]["id"]
    return None

# ============= WELCOME/HOME ROUTE =============

@app.route("/")
def welcome():
    """Welcome page - choose Student or Admin mode"""
    return render_template("welcome.html")

# ============= STUDENT ROUTES =============

@app.route("/student")
def index():
    credentials = data_manager.get_all_credentials()
    progress = get_student_progress()
    current_idx = progress["current_index"]
    completed_ids = set(progress["completed"])
    
    total_count = len(credentials)
    completed_count = len(completed_ids)
    progress_percentage = int((completed_count / total_count) * 100) if total_count > 0 else 0
    
    return render_template(
        "index.html",
        credentials=credentials,
        current_index=current_idx,
        completed_ids=completed_ids,
        total_count=total_count,
        completed_count=completed_count,
        progress_percentage=progress_percentage
    )

@app.route("/learn/<credential_id>")
def learn(credential_id):
    credential = data_manager.get_credential_by_id(credential_id)
    if not credential:
        return redirect(url_for("index"))
    
    progress = get_student_progress()
    is_completed = credential_id in progress["completed"]
    
    results = session.pop("results", None)
    show_next = session.pop("show_next", False)
    next_credential_id = get_next_credential_id(credential_id)
    
    total_count = len(data_manager.get_all_credentials())
    
    return render_template(
        "learn.html",
        credential=credential,
        is_completed=is_completed,
        results=results,
        show_next=show_next,
        next_credential_id=next_credential_id,
        total_count=total_count
    )

@app.route("/check_answers", methods=["POST"])
def check_answers():
    credential_id = request.form.get("credential_id")
    credential = data_manager.get_credential_by_id(credential_id)
    if not credential:
        return redirect(url_for("index"))
    
    results = {}
    all_correct = True
    
    for question in credential["questions"]:
        q_id = question["id"]
        user_answer = request.form.get(q_id)
        
        if question["type"] == "mcq":
            try:
                user_answer_int = int(user_answer)
                is_correct = user_answer_int == question["correct"]
                results[q_id] = {
                    "correct": is_correct,
                    "user_answer": user_answer_int
                }
                if not is_correct:
                    all_correct = False
            except (TypeError, ValueError):
                results[q_id] = {"correct": False, "user_answer": None}
                all_correct = False
                
        elif question["type"] == "input":
            try:
                user_answer_float = float(user_answer)
                tolerance = question.get("tolerance", 0.1)
                is_correct = abs(user_answer_float - question["answer"]) <= tolerance
                results[q_id] = {
                    "correct": is_correct,
                    "user_answer": user_answer_float
                }
                if not is_correct:
                    all_correct = False
            except (TypeError, ValueError):
                results[q_id] = {"correct": False, "user_answer": None}
                all_correct = False
    
    session["results"] = results
    
    if all_correct:
        session["show_next"] = True
        progress = get_student_progress()
        if credential_id not in progress["completed"]:
            progress["completed"].append(credential_id)
            credentials = data_manager.get_all_credentials()
            current_idx = next((i for i, c in enumerate(credentials) if c["id"] == credential_id), None)
            if current_idx is not None:
                progress["current_index"] = min(current_idx + 1, len(credentials) - 1)
    else:
        session["show_next"] = False
    
    return redirect(url_for("learn", credential_id=credential_id))

@app.route("/next/<credential_id>")
def next_module(credential_id):
    next_id = get_next_credential_id(credential_id)
    if next_id:
        return redirect(url_for("learn", credential_id=next_id))
    return redirect(url_for("index"))

@app.route("/reset")
def reset_progress():
    student_progress.clear()
    return redirect(url_for("index"))

# ============= ADMIN ROUTES =============

@app.route("/admin")
def admin_dashboard():
    credentials = data_manager.get_all_credentials()
    return render_template("admin/dashboard.html", credentials=credentials)

@app.route("/admin/credential/new")
def admin_new_credential():
    return render_template("admin/edit_credential.html", credential=None, mode="new")

@app.route("/admin/credential/<credential_id>/edit")
def admin_edit_credential(credential_id):
    credential = data_manager.get_credential_by_id(credential_id)
    if not credential:
        flash("Credential not found", "error")
        return redirect(url_for("admin_dashboard"))
    return render_template("admin/edit_credential.html", credential=credential, mode="edit")

@app.route("/admin/credential/save", methods=["POST"])
def admin_save_credential():
    mode = request.form.get("mode")
    credential_id = request.form.get("credential_id")
    
    # Build credential object from form data
    credential = {
        "title": request.form.get("title"),
        "icon": request.form.get("icon"),
        "objective": request.form.get("objective"),
        "content": {
            "notes": [n.strip() for n in request.form.get("notes", "").split("\n") if n.strip()],
            "images": [],
            "videos": []
        },
        "questions": []
    }
    
    # Parse images
    image_urls = request.form.getlist("image_url")
    image_captions = request.form.getlist("image_caption")
    image_alts = request.form.getlist("image_alt")
    for i in range(len(image_urls)):
        if image_urls[i].strip():
            credential["content"]["images"].append({
                "url": image_urls[i].strip(),
                "caption": image_captions[i].strip() if i < len(image_captions) else "",
                "alt": image_alts[i].strip() if i < len(image_alts) else ""
            })
    
    # Parse videos
    video_titles = request.form.getlist("video_title")
    video_ids = request.form.getlist("video_id")
    video_durations = request.form.getlist("video_duration")
    for i in range(len(video_ids)):
        if video_ids[i].strip():
            credential["content"]["videos"].append({
                "title": video_titles[i].strip() if i < len(video_titles) else "",
                "youtube_id": video_ids[i].strip(),
                "duration": video_durations[i].strip() if i < len(video_durations) else ""
            })
    
    # Parse questions
    question_types = request.form.getlist("question_type")
    question_texts = request.form.getlist("question_text")
    
    for i in range(len(question_texts)):
        if not question_texts[i].strip():
            continue
            
        question = {
            "id": f"q{i+1}",
            "type": question_types[i],
            "question": question_texts[i].strip()
        }
        
        if question_types[i] == "mcq":
            # Get options for this question
            options_key = f"question_{i}_options"
            options = request.form.get(options_key, "").split("\n")
            question["options"] = [opt.strip() for opt in options if opt.strip()]
            
            correct_key = f"question_{i}_correct"
            try:
                question["correct"] = int(request.form.get(correct_key, "0"))
            except ValueError:
                question["correct"] = 0
            
            explanation_key = f"question_{i}_explanation"
            question["explanation"] = request.form.get(explanation_key, "").strip()
            
        elif question_types[i] == "input":
            answer_key = f"question_{i}_answer"
            try:
                question["answer"] = float(request.form.get(answer_key, "0"))
            except ValueError:
                question["answer"] = 0.0
            
            tolerance_key = f"question_{i}_tolerance"
            try:
                question["tolerance"] = float(request.form.get(tolerance_key, "0.1"))
            except ValueError:
                question["tolerance"] = 0.1
            
            hint_key = f"question_{i}_hint"
            question["hint"] = request.form.get(hint_key, "").strip()
        
        credential["questions"].append(question)
    
    # Save credential
    if mode == "new":
        # Generate unique ID
        import time
        credential["id"] = f"cred_{int(time.time())}"
        data_manager.add_credential(credential)
        flash(f"Lesson '{credential['title']}' created successfully!", "success")
    else:
        data_manager.update_credential(credential_id, credential)
        flash(f"Lesson '{credential['title']}' updated successfully!", "success")
    
    return redirect(url_for("admin_dashboard"))

@app.route("/admin/credential/<credential_id>/delete", methods=["POST"])
def admin_delete_credential(credential_id):
    credential = data_manager.get_credential_by_id(credential_id)
    if credential:
        data_manager.delete_credential(credential_id)
        flash(f"Lesson '{credential['title']}' deleted successfully!", "success")
    return redirect(url_for("admin_dashboard"))

if __name__ == "__main__":
    print("\n" + "="*80)
    print("🔌 ELECTRONICS LEARNING PATHWAY - CMS EDITION")
    print("="*80)
    print("\nFEATURES:")
    print("  ✓ Welcome Page - Choose Student or Admin Mode")
    print("  ✓ Student Learning Interface")
    print("  ✓ Admin Content Management System")
    print("  ✓ Dynamic Content (Stored in JSON)")
    print("  ✓ Add/Edit/Delete Lessons")
    print("  ✓ Manage Notes, Images, Videos, Questions")
    print("\nACCESS:")
    print("  Home:    http://127.0.0.1:5000")
    print("  Student: http://127.0.0.1:5000/student")
    print("  Admin:   http://127.0.0.1:5000/admin")
    print("="*80 + "\n")
    
    app.run(debug=True, port=5000)
