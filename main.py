# main.py
from modules.commands import handle_command

def process_command(command_text):
    try:
        response = handle_command(command_text)
        return response if response else "Sorry, I didn’t catch that."
    except Exception as e:
        return f"⚠️ Error processing command: {str(e)}"
