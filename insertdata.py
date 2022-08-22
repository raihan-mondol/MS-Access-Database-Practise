import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\QUPS\Documents\pydb.accdb;'
    conn = pyodbc.connect(con_string)
    print("Connected")

    cursor = conn.cursor()
    myUser = (
        (6, "Mondol", 4, "mondol@gmail.com"),
        (7, "Mondol2", 5,  "mondol2@gmail.com"),
        (8, "Mondol3", 6,  "mondol3@gmail.com")
    )
    cursor.executemany("INSERT INTO users VALUES (?,?,?,?)", myUser)
    conn.commit()
    print("Data Inserted")

except pyodbc.Error as e:
    print(e)
