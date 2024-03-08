#Before the lab Install the python package: pip install mysql-connector
# You will need to have your mysql server up and running,
# I would usually create the database and tables on the server and not through python.
#In this lab I show you how to create the table and then perform the CRUD operations.

# 1. Create a database called wsaa using a python script
import mysql.connector
connection = mysql.connector.connect(
 host="localhost",
 user="root",
 password=""
)
mycursor = connection.cursor()
mycursor.execute("CREATE database wsaa")
mycursor.close()
connection.close()

