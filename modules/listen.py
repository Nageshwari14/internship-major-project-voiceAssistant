import speech_recognition as sr

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()  # important: lowercase for matching
    except sr.UnknownValueError:
        print("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        print("Check your internet connection.")
        return ""
