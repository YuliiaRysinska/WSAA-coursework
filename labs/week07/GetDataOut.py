cursor = db.cursor()
sql="seselect * from student"
values = (1, )

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
    print(x)
cursor.close()
#db.close()