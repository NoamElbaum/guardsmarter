import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="guardsmarter"
)

DB = mycursor = mydb.cursor()

with open('faces/NoamElbaum.jpg', 'rb') as pic:
    face = pic.read()

print(face)

DB.execute(f"insert into residants values(211715966, 3292063, {}, 'Noam', 'Elbaum')")

mydb.commit()