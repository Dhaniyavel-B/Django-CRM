import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'danny',
    passwd = '12345'
)

#create cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE crm")