import socket

client = socket.socket()


def connect():
    global client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(1)
    print('waiting for connection')
    client, address = s.accept()
    print(f'connected to {client}\n{address}')


def alert():
    client.send(bytes("הגיעה התראה משער היישוב נא להגיע במהירות", "utf-8"))


if __name__ == '__main__':
    connect()
    while 1:
        act = input('to alert send a: ')
        if act == 'a':
            alert()
