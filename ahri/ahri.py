import speech_recognition as sr 
import pyttsx3
name = "chiqui"
# Reconoce la voz
listener = sr.Recognizer()
# Voces
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
try:
    with sr.Microphone() as source:
        print("Escuchando...")
        voice = listener.listen (source)
        rec = listener.recognize_google(voice, language='es-ES')
        rec = rec.lower()
        if name in rec:
            talk(rec)
except:
    pass