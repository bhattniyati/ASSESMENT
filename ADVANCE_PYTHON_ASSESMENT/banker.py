import pymysql

# create class name of banker
class Banker:

    # connect database
    mydb= pymysql.connect(host="localhost",user="root",password="",database="Banking_Application")
    mycursor= mydb.cursor()
    
    # create menu
    def Menu(self):
        print("\n\tBanker Menu: ")
        print("\t1).Register")
        print("\t2).Login")
        print("\t3).Update all Customers")
        print("\t4).View all Customers")
        print("\t5).Delete all Customers")

    # create function name of register
    def Register(self,username,password):
        query= "INSERT INTO Banker(username,password) VALUES ('%s','%s')" # insert query
        args=(username, password) # pass arguments
        self.mycursor.execute(query % args) # execute query
        self.mydb.commit() # save data
        print("\n\tBanker Registered Successfully..")

    def Login(self,username,password):
        query= "SELECT * FROM Banker WHERE username = '%s' AND password = '%s'" # insert select query
        args=(username, password)
        self.mycursor.execute(query % args)
        result = self.mycursor.fetchall() # result in fetchall record

        # check condition if result in print login successfully or not so print invalid ..
        if result:
            print("\n\tLogin Successfully..")
        
        else:
            print("\n\tInvalid username or password !!")

    def Update(self,id,name,password):
        query= "update Customer set name='%s', password='%s' where id= '%s'" # insert update query
        args= (name,password,id)
        self.mycursor.execute(query % args)
        self.mydb.commit()
        print("\n\tYour Data Updated Successfully..")

    def View(self):
        query= "SELECT * FROM Customer" # insert select query for view all customer
        self.mycursor.execute(query)
        data=self.mycursor.fetchall()
        print("\t",data) 
    
    def Delete(self,id):
        query= "DELETE FROM Customer WHERE id='%s'" # insert delete query
        args=(id)
        self.mycursor.execute(query % args)
        self.mydb.commit()
        print("\n\tYour Data Deleted Successfully..")

# using inheritance 
# sub class 
class banker2(Banker):

    # create main function
    def main_banker(self):

        # loop
        while True:
                
                self.Menu()
                choice=int(input("\n\tEnter Choice: "))

                if choice==1:
                    username=input("\n\tEnter Username: ")
                    password=input("\tEnter Password: ")
                    self.Register(username,password)

                elif choice==2:
                    username=input("\n\tEnter Username: ")
                    password=input("\tEnter Password: ")
                    self.Login(username,password)

                elif choice==3:
                    id= int(input("\n\tEnter ID: "))
                    name= input("\tEnter Name: ")
                    password= input("\tEnter Password: ")
                    self.Update(id,name,password)

                elif choice==4:
                    self.View()

                elif choice==5:
                    id=int(input("\n\tEnter ID: "))
                    self.Delete(id)

                # choice program continue or not
                r_choice= input("\n\tDo You Want To Perform Press y for yes and n for no: ")
                if r_choice=="n":
                    print("\n\tThank You !!")
                    break


