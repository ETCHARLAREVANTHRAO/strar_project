import time
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import sys
import pyaudio

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wish():
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time < 12:
        talk('Good Morning!')
    elif time >= 12 and time < 18:
        talk("Good Afternoon!")
    else:
        talk("Good Evening!")

    talk("I am STARK. Please tell me how can I help you")


def take_command():

    listener = sr.Recognizer()
    with sr.Microphone() as source:
        talk("I am listening....")
        voice = listener.listen(source)
        try:
            talk("I am Recognizing")

            command = listener.recognize_google(voice)
            return command
        except Exception as e:
            print(e)
            talk("Say that again please")
            return "None"

    return command


if __name__ == '__main__':
    wish()
    while True:
        command = take_command().lower()
        if 'open youtube' in command:
            webbrowser.open("youtube.com")
            continue
        elif 'from wikipedia' in command:
            talk("Getting results from wikipedia ")
            query = command.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            talk("Accoring to wikipedia")
            talk(result)

        elif 'open google' in command:
            webbrowser.open('google.com')

        elif "bye" in command:
            talk("Bye Bye, Thank you")
            exit()

