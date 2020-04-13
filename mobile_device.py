import socket
from playsound import playsound

s = socket.socket()


def connect():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((socket.gethostname(), 1234))
    except ConnectionRefusedError:
        print('no connection')
        connect()
    else:
        print('connected')


connect()

while 1:
    msg = s.recv(1024).decode("utf-8")
    print(msg)
    if msg == "הגיעה התראה משער היישוב נא להגיע במהירות":
        for i in range(2):
            playsound("alert.wav")
    else:
        print('no alerts')
