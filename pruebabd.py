import mysql.connector

connection =mysql.connector.connect(
 host="localhost",
 port="3307",
 user="root",
 password="",
 db="contactos"

)

cursor=connection.cursor()


sql="SELECT * FROM contactos"
cursor.execute(sql)
records=cursor.fetchall()
print("Hay: ", cursor.rowcount,"contactos en la base de datos")

for row in records:
    print("Cotacto Id: ",row[0])
    print("Nombre: ",row[1])
    print("Telefono: ",row[2])
    print("Email: ",row[3])
    print()

cursor.close()
connection.close()