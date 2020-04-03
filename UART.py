import serial

arduino = 'COM11'
fpga = 'COM12'

def open_gate():
    return send_ar('o') & send_fpga('o')


def close_gate():
    return send_ar('c') & send_fpga('c')


def interrupt_check():
    try:
        ser = serial.Serial(arduino, baudrate=9600, timeout=1)
    except serial.serialutil.SerialException:
        return 1
    else:
        res = ser.readline()
        ser.close()
        try:
            res = res.decode('ascii')
        except UnicodeDecodeError:
            print('Com error')
        print(res)
        for i in res:
            if i == 'h':
                for x in range(4):
                    ser.write(b'g')
                return 1
            else:
                return 0


def send_ar(c):
    try:
        ser = serial.Serial(arduino, baudrate=9600, timeout=1)
    except serial.serialutil.SerialException:
        return 0
    else:
        for i in range(4):
            ser.write(c.encode('ascii'))
            res = ser.readline()
        res = res.decode('ascii')
        ser.close()
        print(res)
        if res[0] == c:
            return 1
        else:
            return 0


def send_fpga(c):
    try:
        ser = serial.Serial(fpga, baudrate=9600, timeout=1)
    except serial.serialutil.SerialException:
        return 0
    else:
        for i in range(4):
            ser.write(c.encode('ascii'))
            res = ser.readline()
        res = res.decode('ascii')
        ser.close()
        print(res)
        if res[0] == c:
            return 1
        else:
            return 0


if __name__ == "__main__":
    while 1:
        print('int: ' + str(interrupt_check()))
        if input('close/open: ') == 'c':
            print('result: ' + str(close_gate()))
        else:
            print('result: ' + str(open_gate()))
