import mysql.connector
db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="root",
 database="wsaa"
)
cursor = db.cursor()
sql="insert into student (name, age) values (%s,%s)"
values = ("Mary",21)
cursor.execute(sql, values)
db.commit()
print("1 record inserted, ID:", cursor.lastrowid)
#mycursor.close()
#connection.close()