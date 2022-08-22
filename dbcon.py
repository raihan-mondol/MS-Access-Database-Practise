import pyodbc
import pandas as pd

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\QUPS\Documents\pydb.accdb;'
    conn = pyodbc.connect(con_string)
    print("Connect Successfully")
    cursor = conn.cursor()
    cursor.execute("Select * From users")
    for data in cursor:
        print(data)

    # data = pd.read_sql("Select * From users", conn)
    # print(data)

except pyodbc.Error as e:
    print("Error in Connection", e)

