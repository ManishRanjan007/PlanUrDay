#!C:\Python34\python.exe

from db_Connection import DBConnection as dbConnect

class InsertIntoNotification:
       
        
        def insertNotification(mobileNo, message, timeOfNotification, repeat, enable):
                sql = """INSERT INTO Notification
           (Mobile_No_FK
           ,Message
           ,Time
           ,IsRepeat
           ,IsEnable)
                VALUES ('{0}','{1}','{2}','{3}','{4}')""".format(mobileNo, message, timeOfNotification, repeat, enable)
                print("----------" + sql)
                db, cursor = dbConnect.connectDB()
                cursor.execute(sql)
                db.commit()



class SelectUsersNotifications:
        
       
        def selectNotificationsWhereMobileNo(mobileNo):
                sql = "select * from Notification where Mobile_No_FK = '{0}'".format(mobileNo)
                db, cursor = dbConnect.connectDB()
                cursor.execute(sql)
                userNotifications = []
                for userNotification in cursor:
                        userNotifications.append(userNotification)
                return userNotifications

        def selectAllNotifications():
                sql = "select * from Notification"
                db, cursor = dbConnect.connectDB()
                cursor.execute(sql)
                allNotifations = []
                for userNotification in cursor:
                        allNotifations.append(userNotification)
                return allNotifations
                

        def selectAllNotificationsWhereEnableAndTime(fromTime, toTime):
                sql = """SELECT Id
      ,Mobile_No_FK
      ,Message
      ,date_format(Time, '%H:%i') as time
        ,date_format(Time, '%Y-%m-%d') as date
      ,IsRepeat
      ,IsEnable
        FROM Notification where IsEnable = 'true' and time > date_format('{0}', '%H:%i') and time < date_format('{0}', '%H:%i')""".format(fromTime, toTime)
                print("-----------------")
                print(sql)
              
                db, cursor = dbConnect.connectDB()
                cursor.execute(sql)
                allNotifations = []
                for userNotification in cursor:
                        allNotifations.append(userNotification)
                return allNotifations
        

        
class UpdateNotification:
       

        def updateMsg(mobileNo, message, notificationId):
                sql = """UPDATE Notification
                       SET message = '{0}' where Mobile_Number = '{1}' and Id = '{2}'""".format(message, mobileNo, notificationId)
                print("---------" + sql)
                db, cursor = dbConnect.connectDB()
                cursor.execute(sql)
                db.commit()
                
        def updateNotificationStatus(mobileNo, notificationId, enable):
                sql = """UPDATE Notification
                       SET enable = '{0}' where Mobile_Number = '{1}' and Id = '{2}'""".format(enable, mobileNo, notificationId)
                print("---------" + sql)
                db, cursor = dbConnect.connectDB()
                cursor.execute(sql)
                db.commit()

        
        def updateNotification(notificationId, mobileNo, message, time, repeat, enable):
                sql = """UPDATE Notification
                       SET Message = '{0}', Time = '{1}', Repeat = '{2}', Enable = '{3}' where Id = '{4}' and mobileNo = '{5}'""".format(message, time, repeat, enable, notificationId, mobileNo)
                print("---------" + sql)
                db, cursor = dbConnect.connectDB()
                cursor.execute(sql)
                db.commit()
                
#def printUserdetails(userDetails):
#        for userD in userDetails:
#                print(userD1])


#notifications = SelectUsersNotifications.selectAllNotificationsWhereEnableAndTime("20:23:00", "20:26:00")
#for noti in notifications:
#        print(noti2])
