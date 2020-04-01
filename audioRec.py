import speech_recognition as sr

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


text = Listen()
print(text)