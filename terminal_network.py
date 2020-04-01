import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

client, address = s.accept()
print(f'connected to {client} {address}')



def alert():
    client.send(bytes("come to the gate", "utf-8"))


if __name__ == '__main__':
    while 1:
        act = input('to allert send a: ')
        if act == 'a':
            alert()
