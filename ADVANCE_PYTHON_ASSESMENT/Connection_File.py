import pymysql

# connect database
mydb= pymysql.connect(host="localhost",user="root",password="")
mycursor= mydb.cursor()

# create database name of banking_application
mycursor.execute("create database if not exists Banking_Application")
# save database
mydb.commit()

mydb= pymysql.connect(host="localhost",user="root",password="",database="Banking_Application")
mycursor= mydb.cursor()

# create table name of banker
mycursor.execute("create table if not exists Banker(id int primary key auto_increment, username varchar(20), password varchar(10))")
mydb.commit()

# create table name of customer
mycursor.execute("create table if not exists Customer(id int primary key auto_increment, name varchar(20), password varchar(10), balance float)")
mydb.commit()

