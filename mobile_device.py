import socket
import winsound


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while 1:
    msg = s.recv(1024).decode("utf-8")
    print(msg)
    if msg == 'come to the gate':
        for i in range(2):
            winsound.PlaySound(r"alert.wav", winsound.SND_FILENAME)