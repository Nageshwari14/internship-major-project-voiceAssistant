from modules.jokes import tell_joke
from modules.notes import save_note, show_notes
from modules.history import add_to_history, get_history
import webbrowser
import random
import os
import pyjokes

NOTES_FILE = "user_notes.txt"  # file to store notes persistently


def handle_command(command):
    command = command.lower().strip()

    # Default response
    response = "Sorry, I didn't understand that."

    # Greeting Responses
    if any(greet in command for greet in ["hello", "hi", "hey"]):
        response = random.choice([
            "Hello there! How can I help you today?",
            "Hey! Nice to see you again.",
            "Hi! What can I do for you?"
        ])

    elif "how are you" in command:
        response = random.choice([
            "I'm doing great! Thanks for asking.",
            "Feeling awesome, ready to help you!",
            "All systems running perfectly."
        ])

    elif "i am good" in command or "i'm good" in command or "i am fine" in command:
        response = random.choice([
            "That's wonderful to hear!",
            "Glad you're feeling good! Let's keep it that way!",
            "Awesome! Let's do something productive today."
        ])

    # Jokes (Improved)
    elif "joke" in command:
        try:
            joke = pyjokes.get_joke(language="en", category="neutral")
            response = random.choice([
                f"Here's one for you: {joke}",
                f"Want to laugh? Okay — {joke}",
                f"Alright, get ready... {joke}"
            ])
        except Exception:
            response = tell_joke()

    # Notes (Persistent + Enhanced)
    elif "take note" in command or "save note" in command or "add note" in command:
        note_text = (
            command.replace("take note", "")
            .replace("save note", "")
            .replace("add note", "")
            .strip()
        )
        if not note_text:
            note_text = "Empty note added."

        # Save note to file
        with open(NOTES_FILE, "a", encoding="utf-8") as f:
            f.write(note_text + "\n")

        response = f"Note saved: '{note_text}'"

    elif "show notes" in command or "my notes" in command:
        if not os.path.exists(NOTES_FILE) or os.path.getsize(NOTES_FILE) == 0:
            response = "You don't have any saved notes yet."
        else:
            with open(NOTES_FILE, "r", encoding="utf-8") as f:
                notes = f.readlines()
            formatted_notes = "\n".join([f"{i+1}. {note.strip()}" for i, note in enumerate(notes)])
            response = f"Here are your saved notes:\n{formatted_notes}"

    elif "clear notes" in command or "delete notes" in command:
        if os.path.exists(NOTES_FILE):
            open(NOTES_FILE, "w").close()
            response = "All notes cleared!"
        else:
            response = "No notes found to clear."

    # History
    elif "show history" in command or "command history" in command:
        history_data = get_history()
        if not history_data:
            response = "No history available yet."
        else:
            formatted = "\n".join(
                [f"{i+1}. {h['command']} → {h['response']}" for i, h in enumerate(history_data)]
            )
            response = f"Command history:\n{formatted}"

    # Websites
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        response = "Opening Google."

    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        response = "Opening Facebook."

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        response = "Opening YouTube."

    # Default fallback
    else:
        if "who are you" in command:
            response = "I'm your AI voice assistant — your digital buddy."
        elif "thank you" in command:
            response = "You're most welcome."
        elif "bye" in command:
            response = "Goodbye, see you soon."
        else:
            response = random.choice([
                "Hmm, could you repeat that?",
                "I didn't catch that clearly.",
                "Say that again, please?",
                "Sorry, didn't quite get it."
            ])

    # Add to history every time
    add_to_history(command, response)
    return response
