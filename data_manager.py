import json
import os

# Path to the data file
DATA_FILE = "learning_data.json"

# Initial dataset (existing hardcoded content)
INITIAL_DATA = {
    "credentials": [
        {
            "id": "m1_basics",
            "number": 1,
            "title": "Electricity Basics",
            "icon": "⚡",
            "objective": "Explain electricity, energy, power; Differentiate DC vs AC; Identify conductors and insulators",
            "content": {
                "notes": [
                    "Electricity is the flow of electric charge through a conductor",
                    "Energy is the capacity to do work, measured in Joules (J)",
                    "Power is the rate of energy transfer, measured in Watts (W = J/s)",
                    "DC (Direct Current) flows in one direction; AC (Alternating Current) changes direction periodically",
                    "Conductors allow electricity to flow easily (copper, aluminum)",
                    "Insulators resist electricity flow (plastic, rubber, glass)"
                ],
                "images": [
                    {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Simple_Electrical_Circuit.svg/500px-Simple_Electrical_Circuit.svg.png",
                        "caption": "Simple electrical circuit showing voltage source, switch, and load",
                        "alt": "Basic electrical circuit diagram"
                    },
                    {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Ohm%27s_Law_pie_chart.svg/400px-Ohm%27s_Law_pie_chart.svg.png",
                        "caption": "Ohm's Law relationship: V = I × R",
                        "alt": "Ohm's Law pie chart"
                    }
                ],
                "videos": [
                    {
                        "title": "What is Electricity? - Basics Explained",
                        "youtube_id": "mc979OhitAg",
                        "duration": "3:45"
                    },
                    {
                        "title": "AC vs DC Current - Understanding the Difference",
                        "youtube_id": "j9oDZ3PuW7I",
                        "duration": "5:12"
                    }
                ]
            },
            "questions": [
                {
                    "id": "q1",
                    "type": "mcq",
                    "question": "What is the unit of measurement for electrical power?",
                    "options": ["Volts (V)", "Amperes (A)", "Watts (W)", "Ohms (Ω)"],
                    "correct": 2,
                    "explanation": "Power is measured in Watts (W), which equals Joules per second (J/s)"
                },
                {
                    "id": "q2",
                    "type": "mcq",
                    "question": "Which type of current changes direction periodically?",
                    "options": ["Direct Current (DC)", "Alternating Current (AC)", "Both", "Neither"],
                    "correct": 1,
                    "explanation": "AC (Alternating Current) changes direction periodically, typically 50 or 60 times per second"
                },
                {
                    "id": "q3",
                    "type": "input",
                    "question": "If a device uses 100J of energy in 5 seconds, what is its power consumption in Watts?",
                    "answer": 20.0,
                    "tolerance": 0.5,
                    "hint": "Power = Energy / Time = 100J / 5s"
                }
            ]
        },
        {
            "id": "m1_power",
            "number": 2,
            "title": "Power & Energy Sources",
            "icon": "🔋",
            "objective": "Apply Ohm's Law; Measure voltage, current, and resistance accurately; Calculate power; Select appropriate power sources",
            "content": {
                "notes": [
                    "Voltage (V) is electrical potential difference, measured in Volts",
                    "Current (I) is the flow of electric charge, measured in Amperes (A)",
                    "Resistance (R) opposes current flow, measured in Ohms (Ω)",
                    "Ohm's Law: V = I × R (fundamental relationship)",
                    "Power: P = V × I = I²R = V²/R",
                    "Energy sources: batteries (DC), solar cells, generators, power supplies"
                ],
                "images": [
                    {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Ohm%27s_law_formula_wheel.svg/500px-Ohm%27s_law_formula_wheel.svg.png",
                        "caption": "Ohm's Law formula wheel showing relationships between V, I, R, and P",
                        "alt": "Ohm's Law formula wheel"
                    }
                ],
                "videos": [
                    {
                        "title": "Ohm's Law Explained - Voltage, Current, Resistance",
                        "youtube_id": "HsLLq6Rm5tU",
                        "duration": "4:30"
                    },
                    {
                        "title": "Understanding Power in Electrical Circuits",
                        "youtube_id": "fGM9dTfG4vM",
                        "duration": "6:15"
                    }
                ]
            },
            "questions": [
                {
                    "id": "q1",
                    "type": "mcq",
                    "question": "According to Ohm's Law, if voltage increases and resistance stays constant, what happens to current?",
                    "options": ["Increases", "Decreases", "Stays the same", "Becomes zero"],
                    "correct": 0,
                    "explanation": "From V = I × R, if V increases and R is constant, I must increase proportionally"
                },
                {
                    "id": "q2",
                    "type": "input",
                    "question": "If V = 12V and R = 6Ω, what is the current I in Amperes?",
                    "answer": 2.0,
                    "tolerance": 0.1,
                    "hint": "Use Ohm's Law: I = V / R"
                },
                {
                    "id": "q3",
                    "type": "input",
                    "question": "What is the power (in Watts) dissipated by a 10Ω resistor with 2A current flowing through it?",
                    "answer": 40.0,
                    "tolerance": 0.5,
                    "hint": "Use P = I²R = 2² × 10"
                }
            ]
        },
        {
            "id": "m1_series_parallel",
            "number": 3,
            "title": "Series & Parallel Circuits",
            "icon": "🔌",
            "objective": "Build series and parallel circuits; Apply Kirchhoff's laws; Calculate total resistance",
            "content": {
                "notes": [
                    "Series: Components in a single path; current is same, voltage divides",
                    "Series total resistance: R_total = R1 + R2 + R3 + ...",
                    "Parallel: Components share voltage; current divides",
                    "Parallel total resistance: 1/R_total = 1/R1 + 1/R2 + 1/R3 + ...",
                    "Kirchhoff's Current Law (KCL): Sum of currents into a node = sum of currents out",
                    "Kirchhoff's Voltage Law (KVL): Sum of voltages around a closed loop = 0"
                ],
                "images": [
                    {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Series_circuit.svg/500px-Series_circuit.svg.png",
                        "caption": "Series circuit: Components connected end-to-end in a single path",
                        "alt": "Series circuit diagram"
                    },
                    {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Parallel_circuit.svg/500px-Parallel_circuit.svg.png",
                        "caption": "Parallel circuit: Components connected across common points",
                        "alt": "Parallel circuit diagram"
                    }
                ],
                "videos": [
                    {
                        "title": "Series vs Parallel Circuits Explained",
                        "youtube_id": "VV3dErNFD6c",
                        "duration": "7:20"
                    }
                ]
            },
            "questions": [
                {
                    "id": "q1",
                    "type": "mcq",
                    "question": "In a series circuit with three resistors, what is constant throughout?",
                    "options": ["Voltage", "Current", "Resistance", "Power"],
                    "correct": 1,
                    "explanation": "In series circuits, current is the same through all components"
                },
                {
                    "id": "q2",
                    "type": "input",
                    "question": "Three resistors of 10Ω, 15Ω, and 25Ω are connected in series. What is the total resistance in Ohms?",
                    "answer": 50.0,
                    "tolerance": 0.5,
                    "hint": "In series: R_total = R1 + R2 + R3"
                },
                {
                    "id": "q3",
                    "type": "mcq",
                    "question": "In a parallel circuit, what is the same across all branches?",
                    "options": ["Current", "Resistance", "Voltage", "Power"],
                    "correct": 2,
                    "explanation": "In parallel circuits, voltage is the same across all branches"
                }
            ]
        },
        {
            "id": "m2_breadboard",
            "number": 4,
            "title": "Breadboard Wiring",
            "icon": "🍞",
            "objective": "Wire complex circuits neatly on breadboard; Use power rails correctly; Troubleshoot wiring errors",
            "content": {
                "notes": [
                    "Breadboard allows quick prototyping without soldering",
                    "Vertical columns are connected internally (for power rails)",
                    "Horizontal rows (5 holes) are connected in the center section",
                    "Power rails: red stripe = positive (+), blue/black stripe = ground (-)",
                    "Use color coding: red for power, black for ground, other colors for signals",
                    "Keep wiring neat and organized for easier troubleshooting"
                ],
                "images": [
                    {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Breadboard.jpg/500px-Breadboard.jpg",
                        "caption": "Standard solderless breadboard showing connection pattern",
                        "alt": "Breadboard photo"
                    }
                ],
                "videos": [
                    {
                        "title": "How to Use a Breadboard - Beginner's Guide",
                        "youtube_id": "6WReFkfrUIk",
                        "duration": "5:30"
                    }
                ]
            },
            "questions": [
                {
                    "id": "q1",
                    "type": "mcq",
                    "question": "How many holes are electrically connected in one row of the center section of a standard breadboard?",
                    "options": ["3", "4", "5", "6"],
                    "correct": 2,
                    "explanation": "Standard breadboards have 5 holes connected per row in the center section"
                },
                {
                    "id": "q2",
                    "type": "mcq",
                    "question": "What color wire is conventionally used for ground connections?",
                    "options": ["Red", "Black", "Green", "Yellow"],
                    "correct": 1,
                    "explanation": "Black wire is conventionally used for ground (negative) connections"
                }
            ]
        },
        {
            "id": "m5_digital",
            "number": 5,
            "title": "Digital I/O",
            "icon": "🔌",
            "objective": "Configure pins correctly; Read buttons; Control LEDs; Handle multiple I/O",
            "content": {
                "notes": [
                    "pinMode(pin, mode): Configure pin as INPUT, OUTPUT, or INPUT_PULLUP",
                    "digitalWrite(pin, value): Set output pin HIGH or LOW",
                    "digitalRead(pin): Read input pin state (HIGH or LOW)",
                    "Pull-up resistor: Pulls pin to HIGH when not connected (internal ~20-50kΩ)",
                    "Pull-down resistor: Pulls pin to LOW when not connected",
                    "Debouncing: Software delay or hardware capacitor to eliminate switch bounce"
                ],
                "images": [
                    {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Arduino_Uno_-_R3.jpg/500px-Arduino_Uno_-_R3.jpg",
                        "caption": "Arduino Uno showing digital I/O pins (D0-D13)",
                        "alt": "Arduino Uno board"
                    }
                ],
                "videos": [
                    {
                        "title": "Arduino Digital Input and Output Basics",
                        "youtube_id": "g0pSfyXOXj8",
                        "duration": "8:15"
                    }
                ]
            },
            "questions": [
                {
                    "id": "q1",
                    "type": "mcq",
                    "question": "Which Arduino function is used to set a pin as OUTPUT?",
                    "options": ["digitalWrite()", "digitalRead()", "pinMode()", "setOutput()"],
                    "correct": 2,
                    "explanation": "pinMode() is used to configure a pin as INPUT, OUTPUT, or INPUT_PULLUP"
                },
                {
                    "id": "q2",
                    "type": "mcq",
                    "question": "If a button is connected between a pin and GND, which mode should you use?",
                    "options": ["INPUT", "OUTPUT", "INPUT_PULLUP", "INPUT_PULLDOWN"],
                    "correct": 2,
                    "explanation": "INPUT_PULLUP keeps the pin HIGH when button is not pressed; pressing connects to GND"
                }
            ]
        }
    ]
}

def load_data():
    """Load learning data from file or create initial dataset"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        save_data(INITIAL_DATA)
        return INITIAL_DATA

def save_data(data):
    """Save learning data to file"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_all_credentials():
    """Get all micro-credentials"""
    data = load_data()
    return data.get("credentials", [])

def get_credential_by_id(credential_id):
    """Get a specific credential by ID"""
    credentials = get_all_credentials()
    for cred in credentials:
        if cred["id"] == credential_id:
            return cred
    return None

def add_credential(credential):
    """Add a new credential"""
    data = load_data()
    # Auto-assign number
    credential["number"] = len(data["credentials"]) + 1
    data["credentials"].append(credential)
    save_data(data)
    return credential

def update_credential(credential_id, updated_credential):
    """Update an existing credential"""
    data = load_data()
    for i, cred in enumerate(data["credentials"]):
        if cred["id"] == credential_id:
            # Preserve number and id
            updated_credential["number"] = cred["number"]
            updated_credential["id"] = credential_id
            data["credentials"][i] = updated_credential
            save_data(data)
            return updated_credential
    return None

def delete_credential(credential_id):
    """Delete a credential"""
    data = load_data()
    data["credentials"] = [c for c in data["credentials"] if c["id"] != credential_id]
    # Renumber remaining credentials
    for i, cred in enumerate(data["credentials"]):
        cred["number"] = i + 1
    save_data(data)
    return True
