import serial

ser = serial.Serial('COM7', baudrate=9600, timeout=1)


def open_gate():
    return send('o')


def open_gate():
    return send('c')


def send(c):
    for i in range(4):
        ser.write(c.encode('ascii'))
        res = ser.readline()
    res = res.decode('ascii')
    print(res)
    if (res == 'o'):
        return 1
    else:
        return 0


if __name__ == "__main__":
    while 1:
        send(input('close/open: '))
