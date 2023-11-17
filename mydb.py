import mysql.connector
#import pymysql

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "welcome1"
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE mycompany")

print("All Done!")