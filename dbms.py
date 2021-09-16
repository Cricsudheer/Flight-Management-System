import mysql.connector


#for connecting to our database using python

lib_database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sudheer123#",
    database='Flight-Management-System',
)

