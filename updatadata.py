import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\QUPS\Documents\pydb.accdb;'
    conn = pyodbc.connect(con_string)
    print("connected")

    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ? WHERE roll = ?", ('raihanmondol', 1))
    conn.commit()
    print("Data Updated")

except pyodbc.Error as e:
    print(e)