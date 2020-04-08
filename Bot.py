import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os


def speak(text):
    out = gTTS(text=text, lang='en', slow=False)
    out.save('play.mp3')
    playsound("play.mp3")
    os.remove("play.mp3")


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='he')
            return text
        except:
            print("Sorry could not recognize what you said")


if __name__ == '__main__':
    speak('hello what is your name')
    print('name: ')
    text = listen()
    print(text)
