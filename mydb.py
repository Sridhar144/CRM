import mysql.connector
database=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Sridhar4444!'
)
#perpare a cursor obj
cursorObject=database.cursor()
#creatw a database
cursorObject.execute("CREATE DATABASE sridhar")

print("done")