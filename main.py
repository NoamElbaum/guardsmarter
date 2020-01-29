import plate
import face_rec

num = plate.read_plate('plate2.jpg')
name = face_rec.classify_face('test3.jpg')
print(f'plate: {num}\nname: {name}')
while 1:
    pass