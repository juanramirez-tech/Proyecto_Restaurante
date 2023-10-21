import sqlite3

try:
    mi_conexion = sqlite3.connect("database/Carnivoros.db")
    cursor = mi_conexion.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as ex:
    print(ex)

