import socket
from playsound import playsound


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
print('connected')

while 1:
    msg = s.recv(1024).decode("utf-8")
    print(msg)
    if msg == 'come to the gate':
        for i in range(2):
            playsound("alert.wav")
    else:
        print('no alerts')