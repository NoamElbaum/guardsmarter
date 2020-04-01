from win32com.client import Dispatch


def Robo(text):
    robo = Dispatch("SAPI.SpVoice")
    robo.Speak(text)


Robo("Hello")