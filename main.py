from datetime import datetime
import plateRec
import face_rec
import sql_interface as sql
import terminal_network as tour
import UART
import Bot

last_plate = 0
coming_plate = 1
plates = sql.read('car_num')
plates = plates[0]
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
        coming_plate = plateRec.read_plate('plates/plate1.png')  # take plate photo
        print('waiting for car')

    for p in plates:
        if coming_plate == p:
            car_num = p
        else:
            car_num = 0

    if car_num == 0:

        if UART.interrupt_check():
            tour.alert()

        pass  # add bot here
    else:
        face_id = face_rec.classify_face('test_faces/test.jpg')  # take face photo
        registered_plate_id = sql.read_where('ID', f'car_num = {p}')
        if face_id == registered_plate_id:
            print('opened')
            UART.open_gate()
            log(face_id)
        else:
            pass  # add bot here
