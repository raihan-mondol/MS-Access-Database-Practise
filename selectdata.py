import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\QUPS\Documents\pydb.accdb;'
    conn = pyodbc.connect(con_string)
    print("connected")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    for data in cursor.fetchall():
        print(data)

except pyodbc.Error as e:
    print(e)
