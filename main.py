from datetime import datetime
import plate_rec
import face_rec
import sql_interface as sql
import terminal_network as tour
import UART
import Bot
import time

last_plate = 0
coming_plate = 1
plates = sql.read('car_num')
names = sql.read('f_name')

f_names = []
ynList = ["כן", "לא"]

for n in names:
    f_names.append(n[0])

tempID = sql.read('ID')
ID = []
for n in tempID:
    ID.append(n[0])

print(f_names)

print('plates: ' + str(plates))


def log(id, plate):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S.%f")
    name = sql.read_where("f_name, l_name", f"id = {id}")
    name = name[0][0] + ' ' + name[0][1]
    data = (date, plate, name, id)
    print(data)
    sql.write("""insert into entries_log values(%s, %s, %s, %s)""", data)


while 1:

    while coming_plate != last_plate:
        coming_plate = plate_rec.read_plate('plates/plate1.png')  # take plate photo
        print('waiting for car')

    for p in plates:
        if coming_plate == p[0]:
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
                UART.open_gate();
                time.sleep(10)
            else:  # not in the name list
                tour.alert()



    else:  # num wworking face not working
        face_id = face_rec.classify_face('test_faces/test.jpg')  # take face photo
        registered_plate_id = sql.read_where('ID', f'car_num = {p}')
        if face_id == registered_plate_id:
            print('opened')
            UART.open_gate()
            log(face_id)
        else:
            Bot.speak(
                "Hello welcome to guardsmarter!  your face is not matching the correct plate number, is this your car?")
            carValidate = Bot.listen()  # Waiting for yes or no
            if carValidate == ynList[0]:
                Bot.speak("Ok, may i have your personal ID number?")
                clientID = Bot.listen()
                # insert id check
            else:
                Bot.speak("Please wait for a guard to come.")
                tour.alert()
