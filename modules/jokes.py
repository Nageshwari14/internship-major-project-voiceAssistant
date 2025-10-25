import pyjokes
from .speak import speak

def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)
