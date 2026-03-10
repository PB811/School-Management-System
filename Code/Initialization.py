import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "ilkr1475")
if mydb.is_connected():
     print("Successfully Connected")
mycursor = mydb.cursor()
logs = ""
mycursor.execute("show databases")
logs += str(mycursor)
for i in mycursor:
 	print(i)
print()
'''
mycursor.execute("create database SMS") #executed at the time of creation
for i in mycursor:
 	print(i)
print()
'''
mycursor.execute("use SMS")
logs += str(mycursor)
for i in mycursor:
 	print(i)
print()	
