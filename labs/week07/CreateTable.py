import mysql.connector

db = mysql.connector.connect(
 host=" localhost ",
 user=" user ",
 password=" root ",
 database="wsaa"
)
mycursor = db.cursor()
sql="CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"
mycursor.execute(sql)
mycursor.close()
db.close()
