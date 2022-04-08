import speech_recognition as sr
import pyttsx3
# import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
# engine.say("I am your alexa")
# engine.say("What can I do for you")
# engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def alexa_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = alexa_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("Playing" + song)
        print(song)
        # pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("Current time is" + time)
    elif "superstar" in command:
        person = command.replace("superstar","")
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif "joke" in command:
        talk(pyjokes.get_joke())
run_alexa()