from datetime import datetime
import plate_rec
import face_rec
import sql_interface as sql
import terminal_network as tour
import UART
import Bot
import time

last_plate = 0
coming_plate = 0
car_num = 0
plates = sql.read('car_num')
f_names = sql.read('f_name')
ID = sql.read('ID')

ynList = ["כן", "לא"]

print(f_names)
print(ID)
print('plates: ' + str(plates))

tour.connect()


def log(id, plate):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S.%f")
    name = sql.read_where("f_name, l_name", f"id = {id}")
    name = name[0][0] + ' ' + name[0][1]
    data = (date, plate, name, id)
    print(data)
    sql.write("""insert into entries_log values(%s, %s, %s, %s)""", data)


while 1:

    while coming_plate == last_plate:
        num = plate_rec.read_plate('plates/plate1.png')  # take plate photo
        if num < 10000000:
            coming_plate = num
        print('waiting for car')

    for p in plates:
        if coming_plate == p:
            car_num = p
        else:
            car_num = 0

    if car_num == 0:  # plate num not working
        Bot.speak("Hello, Welcome to guardsmarter!, What is your name?")
        Bot.speak("If u have issues u can press the emergency button for help")
        if UART.interrupt_check():
            tour.alert()
        clientName = Bot.listen()
        for name in f_names:
            if name == clientName:  # in the name list
                UART.open_gate()
                client_id = sql.read_where('ID', f'F_name = {name}')
                log(client_id, coming_plate)
                time.sleep(10)
                UART.close_gate()
            else:  # not in the name list
                tour.alert()

    else:
        face_id = face_rec.classify_face('test_faces/test.jpg')  # take face photo
        registered_plate_id = sql.read_where('ID', f'car_num = {car_num}')
        if face_id == registered_plate_id:
            print('opened')
            UART.open_gate()
            log(face_id, car_num)
        else:               # num working face not working
            Bot.speak("Hello welcome to guardsmarter!  your face is not matching the correct plate number, is this your car?")
            carValidate = Bot.listen()  # Waiting for yes or no
            if carValidate == ynList[0]:
                Bot.speak("Ok, may i have your personal ID number?")
                clientID = Bot.listen()
                for cID in ID:
                    if cID == clientID:  # ID match
                        log(clientID, car_num)
                        UART.open_gate()
                        time.sleep(10)
                        UART.close_gate()
                    else:  # ID does not match
                        tour.alert()
            else:
                Bot.speak("Please wait for a guard to come.")
                tour.alert()
