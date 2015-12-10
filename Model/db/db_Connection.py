#!C:\Python34\python.exe

import pymysql as conn
#import mysql.connector as conn
#from mysql.connector import Error

class DBConnection:
       
        def connectDB():
            
            hostname = 'localhost'
            database = 'planurday'
            username = 'planurday1'
            password = 'planurday1'
           
            db = conn.connect( user=username, password=password,host = hostname, database=database)
            cursor = db.cursor()
           
            #tables = cursor.execute('show tables')
            #print(db)
            #tables = cursor.execute('commit')
            #db.commit()
           # print(tables)
            #sql = "select * from user_info"
            #output = cursor.execute(sql)
            #for row in cursor:
            #       print(row)
            #print(cursor.description)
            return db,cursor



#DBConnection.connectDB()
        

    
