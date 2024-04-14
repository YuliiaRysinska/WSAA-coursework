import mysql.connector
#import dbconfig as cfg
class StudentDAO:
      host =""
      user = ""
      password =""
      database =""
      connection = ""
      cursor =""
      
def __init__(self):
#these should be read from a config file
        self.host="localhost"
        self.user="root"
        self.password=""
        self.database="wsaa"
        
def getCursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

def closeAll(self):
        self.connection.close()
        self.cursor.close()
        
def create(self, values):
        cursor = self.getCursor()
        sql="insert into student (name, age) values (%s,%s)"
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

def getAll(self):
        cursor = self.getcursor()
        sql="select * from student"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))


def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from sdudent where id = 2"
        values = (id,)
        
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

def update(self, values):
        cursor = self.getcursor()
        sql="update book set title= %s,author=%s, price=%s  where id = %s"
        
        #values = (student.get("title"), student.get("author"), book.get("price"),id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        

def delete(self, id):
        cursor = self.getcursor()
        sql="delete from book where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        

def convertToDictionary(resultLine):
        studentKeys=['id','name', 'age']
        student = {}
        currentkey = 0
        for attrib in resultLine:
            student[studentKeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return student
        
studentDAO = StudentDAO()