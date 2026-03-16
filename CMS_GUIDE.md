# 📚 Content Management System (CMS) Guide

## Overview

The Electronics Learning Platform now includes a **Content Management System** that allows administrators and instructors to dynamically add, edit, and manage learning content without modifying code.

---

## 🔑 Key Features

### Dynamic Content Management
- ✅ Add new lessons
- ✅ Edit existing lessons
- ✅ Delete lessons
- ✅ Manage notes/explanations
- ✅ Add/remove images
- ✅ Add/remove YouTube videos
- ✅ Create assessment questions (MCQ & Input)
- ✅ Set correct answers and explanations

### Data Storage
- Content stored in **`learning_data.json`**
- Existing hardcoded content used as **initial dataset**
- Easy to backup and restore
- Human-readable JSON format

---

## 🚀 Quick Start

### Access the Admin Panel

1. **Start the application:**
   ```bash
   python app.py
   ```

2. **Access URLs:**
   - **Student View**: `http://127.0.0.1:5000`
   - **Admin Panel**: `http://127.0.0.1:5000/admin`

---

## 📖 Using the CMS

### Admin Dashboard

**What You See:**
- Total number of lessons
- List of all lessons with:
  - Lesson number
  - Icon
  - Title
  - Content counts (notes, images, videos, questions)
  - Edit and Delete buttons

**Actions:**
- Click **"+ Add New Lesson"** to create new content
- Click **"Edit"** to modify existing lessons
- Click **"Delete"** to remove lessons (with confirmation)
- Click **"← Back to Student View"** to see student interface

---

## ✏️ Creating/Editing Lessons

### Basic Information

**1. Lesson Title** (Required)
- Enter the name of the lesson
- Example: "Electricity Basics"

**2. Icon** (Required)
- Single emoji to represent the lesson
- Example: ⚡

**3. Learning Objectives** (Required)
- List what students will learn
- **Format**: Separate with semicolons (;)
- **Example**: 
  ```
  Explain electricity, energy, power; Differentiate DC vs AC; Identify conductors and insulators
  ```
- These become bullet points on the lesson card

### Notes & Explanations

**Key Concepts** (Required)
- Enter each note on a new line
- Each line becomes a separate bullet point
- Example:
  ```
  Electricity is the flow of electric charge
  Energy is the capacity to do work
  Power is the rate of energy transfer
  ```

### Images

**Add Images:**
1. Click **"+ Add Image"**
2. Fill in:
   - **Image URL**: Full URL to the image
   - **Caption**: Description shown below image
   - **Alt Text**: Accessibility text
3. Click **"+ Add Image"** again for more images
4. Click **"Remove"** to delete an image

**Example:**
- URL: `https://example.com/circuit.png`
- Caption: `Simple electrical circuit diagram`
- Alt: `Basic circuit with battery and resistor`

### YouTube Videos

**Add Videos:**
1. Click **"+ Add Video"**
2. Fill in:
   - **Video Title**: Descriptive title
   - **YouTube ID**: The ID from YouTube URL
   - **Duration**: Length of video (e.g., "5:30")
3. Click **"+ Add Video"** again for more
4. Click **"Remove"** to delete a video

**Getting YouTube ID:**
- From URL: `youtube.com/watch?v=VIDEO_ID_HERE`
- Example: If URL is `youtube.com/watch?v=dQw4w9WgXcQ`
- Use: `dQw4w9WgXcQ`

### Assessment Questions

**Add Questions:**
1. Click **"+ Add Question"**
2. Select question type:
   - **Multiple Choice (MCQ)**
   - **Numerical Input**

**For Multiple Choice Questions:**
- **Question Text**: The question
- **Options**: Enter each option on a new line
- **Correct Option Index**: 0 for first option, 1 for second, etc.
- **Explanation**: Why this answer is correct

**Example MCQ:**
```
Question: What is the unit of power?
Options (one per line):
Volts
Amperes
Watts
Ohms

Correct Index: 2
Explanation: Power is measured in Watts (W)
```

**For Numerical Input Questions:**
- **Question Text**: The question
- **Correct Answer**: Numerical value
- **Tolerance**: Acceptable range (e.g., ±0.5)
- **Hint**: Help text if answer is wrong

**Example Input Question:**
```
Question: If V=12V and R=6Ω, what is current I?
Answer: 2.0
Tolerance: 0.1
Hint: Use Ohm's Law: I = V / R
```

### Saving

1. Click **"Create Lesson"** or **"Save Changes"**
2. You'll be redirected to dashboard
3. Success message will confirm the save

### Canceling

- Click **"Cancel"** to discard changes
- Returns to admin dashboard

---

## 🗑️ Deleting Lessons

1. On admin dashboard, click **"Delete"** next to lesson
2. Confirm deletion in popup
3. Lesson is removed
4. Remaining lessons are renumbered automatically

---

## 💾 Data Storage

### File Location
**`learning_data.json`** in the same directory as `app.py`

### Initial Dataset
- First time running: Creates `learning_data.json` with 5 existing lessons
- All hardcoded content becomes the starting dataset
- File is human-readable and editable

### Data Structure
```json
{
  "credentials": [
    {
      "id": "unique_id",
      "number": 1,
      "title": "Lesson Title",
      "icon": "⚡",
      "objective": "Learning goals",
      "content": {
        "notes": ["Note 1", "Note 2"],
        "images": [
          {
            "url": "image URL",
            "caption": "Description",
            "alt": "Alt text"
          }
        ],
        "videos": [
          {
            "title": "Video title",
            "youtube_id": "VIDEO_ID",
            "duration": "5:30"
          }
        ]
      },
      "questions": [
        {
          "id": "q1",
          "type": "mcq",
          "question": "Question text",
          "options": ["Option 1", "Option 2"],
          "correct": 0,
          "explanation": "Why correct"
        }
      ]
    }
  ]
}
```

---

## 🔄 Backup & Restore

### Backup
```bash
# Make a copy of your data
cp learning_data.json learning_data_backup.json
```

### Restore
```bash
# Restore from backup
cp learning_data_backup.json learning_data.json
```

### Reset to Original
```bash
# Delete data file - will recreate with initial dataset on next run
rm learning_data.json
python app.py
```

---

## 🎯 Best Practices

### Content Quality
- ✅ Write clear, concise notes
- ✅ Use high-quality images (ideally from Wikimedia Commons)
- ✅ Test YouTube videos to ensure they're public
- ✅ Write fair, educational questions
- ✅ Provide helpful explanations and hints

### Organization
- ✅ Order lessons from basic to advanced
- ✅ Keep objectives focused (3-5 per lesson)
- ✅ Include variety: notes, images, videos
- ✅ Balance question difficulty

### Technical
- ✅ Use full URLs for images (starting with `https://`)
- ✅ Test all content before publishing
- ✅ Backup `learning_data.json` regularly
- ✅ Use descriptive titles and captions

---

## ❓ FAQ

**Q: Can I edit the JSON file directly?**
A: Yes! `learning_data.json` is plain text. Just ensure valid JSON syntax.

**Q: What happens if I delete all lessons?**
A: The dashboard will show "No lessons found" with an option to create new ones.

**Q: Can multiple admins edit simultaneously?**
A: No - current version doesn't support concurrent editing. Last save wins.

**Q: Where are student progress data stored?**
A: Currently in memory (resets on server restart). For production, implement database storage.

**Q: Can I import lessons from another system?**
A: Yes - if you can convert to the JSON format shown above, paste into `learning_data.json`.

**Q: How do I change lesson order?**
A: Currently auto-ordered by creation. To reorder, edit the JSON file and change the "number" fields.

---

## 🛡️ Security Notes

**Important:**
- This CMS has NO authentication/authorization
- Anyone with the `/admin` URL can edit content
- **For production**: Add login system
- **Recommendation**: Restrict admin panel to trusted IPs

**Simple Protection:**
```python
# Add to app.py before admin routes
@app.before_request
def restrict_admin():
    if request.path.startswith('/admin'):
        # Add password check here
        # Or check user session
        # Or restrict by IP
        pass
```

---

## 🔧 Troubleshooting

**Problem: Changes not appearing**
- Solution: Refresh browser with Ctrl+F5
- Check: `learning_data.json` was updated

**Problem: JSON error on save**
- Solution: Check admin form for empty required fields
- Check: Special characters in text fields

**Problem: Images not loading**
- Solution: Verify image URLs are public and accessible
- Check: URL starts with `https://`

**Problem: Videos not playing**
- Solution: Verify YouTube ID is correct
- Check: Video is public, not private

---

## 📝 Example Workflow

### Adding a New Lesson

1. **Access Admin** → `http://127.0.0.1:5000/admin`

2. **Click** → "+ Add New Lesson"

3. **Fill Basic Info:**
   - Title: "LED Control"
   - Icon: 💡
   - Objectives: "Control LED brightness; Use PWM; Understand duty cycle"

4. **Add Notes:**
   ```
   LEDs emit light when current flows through them
   PWM controls brightness by switching on/off rapidly
   Duty cycle is the percentage of time signal is HIGH
   ```

5. **Add Image:**
   - URL: `https://example.com/led.jpg`
   - Caption: "LED circuit with Arduino"
   - Alt: "LED connected to pin 13"

6. **Add Video:**
   - Title: "PWM LED Control Tutorial"
   - ID: `abc123xyz`
   - Duration: "4:15"

7. **Add Question:**
   - Type: Multiple Choice
   - Question: "What does PWM stand for?"
   - Options:
     ```
     Power Width Modulation
     Pulse Width Modulation
     Pulse Wave Measurement
     Power Wave Measurement
     ```
   - Correct: 1
   - Explanation: "PWM stands for Pulse Width Modulation"

8. **Save** → Success!

---

## 🎓 Summary

The CMS makes it easy to:
- ✅ Manage all learning content dynamically
- ✅ Add lessons without coding
- ✅ Update existing content
- ✅ Organize educational materials
- ✅ Create assessments
- ✅ Maintain flexibility

**No code changes required - just use the admin interface!**

---

**Happy Content Creating! 📚✨**
