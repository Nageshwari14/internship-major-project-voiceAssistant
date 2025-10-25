import json
import os

NOTES_FILE = "modules/notes.json"

def save_note(note_text):
    notes = []
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            notes = json.load(f)
    notes.append(note_text)
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)
    return "📝 Note saved successfully!"

def show_notes():
    if not os.path.exists(NOTES_FILE):
        return "No notes found yet."
    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)
    if not notes:
        return "No notes found yet."
    return "🗒️ Your notes:\n" + "\n".join(f"{i+1}. {n}" for i, n in enumerate(notes))
