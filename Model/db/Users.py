#!C:\Python34\python.exe

from db_Connection import DBConnection as dbConnect

class InsertIntoUsers:
       
        
        def insertUsers(firstname, lastname, mobileno, dob, emailid, password):
                sql = """INSERT INTO User_Info
           (First_Name
           ,Last_Name
           ,Mobile_Number
           ,DOB
           ,EmailID
           ,Password) values ('{0}','{1}','{2}','{3}','{4}','{5}')""".format(firstname, lastname, mobileno, dob, emailid, password)
                print("----------" + sql)
                db, cursor = dbConnect.connectDB()
                cursor.execute(sql)
                db.commit()



class SelectUsers:
        
       
        def selectUserWhereMobileNo(mobileNo, password):
                sql = "select * from User_Info where Mobile_Number = '{0}' and password = '{1}'".format(mobileNo, password)
                print(";;;;;;;;;;;;;;;;;;;;;;;;;;")
                print(sql)
                db,cursor = dbConnect.connectDB()
                cursor.execute(sql)
                userDetails = []
                for userDetail in cursor:
                        userDetails.append(userDetail)
                return userDetails

        def selectAllUsers():
                sql = "select * from User_Info"
                db, cursor = dbConnect.connectDB()
                cursor.execute(sql)
                userDetails = []
                for userDetail in cursor:
                        userDetails.append(userDetail)
                return userDetails
        
class UpdateUsers:
       

        def updatePassword(mobileNo, newPassword):
                sql = """UPDATE User_Info
                       SET Password = '{0}' where Mobile_Number = '{1}'""".format(newPassword, mobileNo)
                print("---------" + sql)
                db, cursor = dbConnect.connectDB()
                cursor.execute(sql)
                db.commit()
                

def printUserdetails(userDetails):
        for userD in userDetails:
                print(userD1)


#printUserdetails(SelectUsers.selectUserWhereMobileNo('7894561230'))
#updateUsers.updatePassword('7894561230','78787')              
#InsertIntoUsers.insertUsers('Manish', 'Ranjan', '7894561230' , '2012-07-24', 'manishranjan007@gmail.com', 'manish_1992')
