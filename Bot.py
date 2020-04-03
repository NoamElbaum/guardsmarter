from win32com.client import Dispatch
import speech_recognition as sr

def Robo(text):
    robo = Dispatch("SAPI.SpVoice")
    robo.Speak(text)


def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hello, please say your name :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,  language='he')
            return text
        except:
            print("Sorry could not recognize what you said")



Robo("Hello")