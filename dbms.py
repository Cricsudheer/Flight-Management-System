import mysql.connector
import  users

#connecting to our database using python

flight_manager = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sudheer123#",
    database='Flight-Management-System',
)

#cursor for traversing in the database


my_cursor = flight_manager.cursor()


#passing user and admin objects

def give_user_admin():
    user = users.users(flight_manager)
    admin = users.admins(flight_manager)

    me =user
    sup = admin
    return [me, sup]
