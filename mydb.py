import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
)



cursorObject = dataBase.cursor()
 
 #create database
cursorObject.execute("Create DATABASE CRMDB")

print("All done!")