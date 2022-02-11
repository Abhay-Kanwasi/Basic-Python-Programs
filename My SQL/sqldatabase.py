import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "abhay",
    password = "alex4617p",
    port = 3306
)

print(mydb)