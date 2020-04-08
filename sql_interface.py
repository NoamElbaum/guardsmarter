import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="guardsmarter",
    use_pure=True
)

DB = mydb.cursor()


def add_resident(ID, carNum, picPath, f_name, l_name):
    with open(picPath, 'rb') as pic:
        face = pic.read()
    print(face)
    query = """insert into residents values(%s, %s,%s,%s,%s)"""
    data = (ID, carNum, face, f_name, l_name)
    DB.execute(query, data)

    mydb.commit()


def read(select_frase):
    DB.execute(f"SELECT {select_frase} from guardsmarter.residents;")
    data = DB.fetchall()
    return data


def read_where(select_frase, where_frase):
    DB.execute(f"SELECT {select_frase} from guardsmarter.residents where {where_frase};")
    data = DB.fetchall()
    return data


def write(query, data):
    DB.execute(query, data)
    mydb.commit()


if __name__ == '__main__':
    id_num = int(input('enter residents id: '))
    car_num = int(input('enter car num: '))
    img_path = str(input('enter pic path: '))
    f_name = str(input('enter first name: '))
    l_name = str(input('enter last name: '))

    add_resident(id_num , car_num, img_path, f_name, l_name)
    read('pic')
