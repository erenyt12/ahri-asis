import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
name = "chiqui"
# Reconoce la voz
listener = sr.Recognizer()
# Voces
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Le pasamos un texto
def talk(text):
    """ Le habamos y lo pasa a texto """
    engine.say(text)
    engine.runAndWait()
def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen (source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, "")
                print(rec)
    except:
        pass
    return rec

# Asignando variables y reproduciendo en YT
def run():
    """ Se le asigna a la variable rec
    lo que salga de listen """
    rec = listen()
    if 'reproducí' in rec:
        musica = rec.replace('reproducí', '')
        talk('Reproduciendo' + musica)
        pywhatkit.playonyt(musica)
    if 'hora' in rec:
        hora = datetime.datetime().now().strftime('%H:%M')
        talk("Son las " + hora)

# Utilizando la fn
run()