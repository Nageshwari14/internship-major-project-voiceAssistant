# Internship Major Project: Voice-Controlled AI Assistant

## Project Overview
This project is a **voice-controlled AI assistant** designed to respond to both **text and voice commands**. It is built using **Python, Flask, and JavaScript**, and features a **chat-based interface** similar to WhatsApp, where all conversations are displayed and saved during the session.

The assistant can:
- Respond to greetings
- Tell jokes
- Take and display notes
- Maintain command history
- Open websites like Google, YouTube, and Facebook
- Speak responses using text-to-speech

The goal of this project is to provide a friendly, interactive AI assistant that works smoothly with various accents and voice volumes, and provides an intuitive, visually appealing frontend.

---

## Features

1. **Text & Voice Commands**
   - Users can type commands in the chat input box or speak using a microphone.
   - Voice input is processed in real-time and the assistant responds both visually in the chat and through speech output.

2. **Jokes**
   - Users can ask the assistant to tell jokes.
   - The assistant randomly selects a joke from its pre-defined list.

3. **Notes Management**
   - Users can save notes by typing commands like "take note" or "add note."
   - All notes are displayed when requested using commands like "show notes."
   - Notes are shown in the chat interface so users can see them like a conversation.

4. **Command History**
   - Every command given to the assistant is recorded along with its response.
   - Users can view the full command history during the session.

5. **Website Access**
   - Users can ask the assistant to open websites such as Google, YouTube, and Facebook.
   - The assistant opens the requested site in the default web browser.

6. **Interactive Frontend**
   - Chat interface with message bubbles for both user and assistant.
   - Includes a microphone button for voice input and a send button for text.
   - Conversations remain visible throughout the session like a WhatsApp chat.

7. **Voice Output**
   - All responses from the assistant are spoken using text-to-speech.
   - Supports multiple accents and voice frequencies for better recognition.

---

## How the Project Works

1. **Frontend**
   - Built with HTML, CSS, and JavaScript.
   - Displays messages in a chatbox and handles user input.
   - Uses browser’s speech recognition API to capture voice commands.
   - Sends commands to the backend and receives responses.

2. **Backend**
   - Built with **Python** and **Flask**.
   - Exposes an API endpoint to receive commands from the frontend.
   - Processes commands using the main command handler and returns a response.

3. **Command Handling**
   - Commands are processed using a centralized handler.
   - The handler interprets the command and decides which action to perform:
     - Greeting, joke, note, history, or website opening.
   - Adds every command-response pair to a session-based history.
   - Returns the response to the frontend to display and speak.

4. **Voice Recognition & Speech**
   - Uses the browser’s speech recognition API to capture voice input.
   - Uses the browser’s speech synthesis API to speak the assistant’s responses.
   - Designed to handle different accents, frequencies, and volumes.

---

## How to Run the Project

### Prerequisites
- **Python 3.x** installed
- **Web browser** (Chrome recommended)
- **Internet connection** (for some APIs like Wikipedia or websites)

### Steps

1. **Set up the Python environment**
   - Create and activate a virtual environment (optional but recommended).

2. **Install dependencies**
   - Install required Python packages like `Flask`, `Flask-CORS`, `requests`, `wikipedia`, `pyttsx3`, and `SpeechRecognition`.

3. **Start the backend**
   - Run the Flask app to serve API requests from the frontend.

4. **Open the frontend**
   - Open the HTML file in your browser.
   - You will see a chat interface with a text box, send button, and microphone button.

5. **Use the assistant**
   - Type a command or click the microphone to speak.
   - Assistant responds visually and verbally.
   - All messages remain visible in the chat box during the session.

---

## Usage Examples

- **Greetings**
  - User: "Hello"
  - Assistant: "Hello! How can I help you today?"

- **Jokes**
  - User: "Tell me a joke"
  - Assistant: "Why do programmers prefer dark mode? Because light attracts bugs!"

- **Notes**
  - User: "Take note Buy groceries"
  - Assistant: "Note saved: Buy groceries"
  - User: "Show notes"
  - Assistant displays all saved notes in the chat.

- **History**
  - User: "Show history"
  - Assistant displays all past commands and responses.

- **Websites**
  - User: "Open Google"
  - Assistant opens Google in the default browser and responds with "Opening Google".

---

## Project Structure

- **Frontend**: Handles user interface and voice input.
- **Modules**: Contains command logic, jokes, notes, and history.
- **Backend (Flask)**: Receives commands, processes them, and sends responses.
- **Main Processor**: Connects frontend commands to command handling logic.

---

## Future Improvements

- Add more commands and integrations (weather, reminders, etc.)
- Use NLP models for smarter responses
- Store notes and history in a database for persistence across sessions
- Enhance voice recognition for noisy environments

---

**Author:** Nageshwari Hinde  
**Project:** Internship Major Project – Voice-Controlled AI Assistant
