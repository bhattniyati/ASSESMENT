import pymysql

# create class name of customer
class Customer:

    # connect database
    mydb= pymysql.connect(host="localhost",user="root",password="",database="Banking_Application")
    mycursor= mydb.cursor()

    # dunder method
    def __init__(self):
        self.balance=0.0
    
    # create menu
    def Menu(self):
            print("\n\tCustomer Menu: ")
            print("\t1).Register")
            print("\t2).Login")
            print("\t3).Can Withdraw Amount")
            print("\t4).Can deposit amount")
            print("\t5).Can view balance")

    # create function name of register
    def Register(self,name,password,balance):
        query= "INSERT INTO Customer(name,password,balance) VALUES ('%s','%s','%s')" # insert query
        args=(name,password,balance) # pass arguments
        self.mycursor.execute(query % args) # execute query
        self.mydb.commit() # save data
        print("\n\tBanker Registered Successfully..")

    def Login(self,name,password):
        query= "SELECT * FROM Customer WHERE name = '%s' AND password = '%s' " # insert select query
        args=(name,password)
        self.mycursor.execute(query % args)
        result = self.mycursor.fetchall() # result in fetchall record

        # check condition if result in print login successfully or not so print invalid ..
        if result:
            print("\n\tLogin Successfully..")
        
        else:
            print("\n\tInvalid username or password !!")
        
    def Withdraw(self,id,balance):
        query= "SELECT balance from Customer WHERE id='%s'" # insert select query
        args=(id)
        self.mycursor.execute(query % args)
        total= self.mycursor.fetchone()[0] - balance # fetch one row/single record and - balance
        query="UPDATE Customer SET balance= '%s' WHERE id='%s'" # insert update query
        args=(total,id)
        self.mycursor.execute(query % args)
        self.mydb.commit()
        print(f"\tDeposite of {balance} for {id} Successful..")

    def Deposite(self,id,balance):
        query= "SELECT balance from Customer WHERE id='%s'" # insert select query
        args=(id)
        self.mycursor.execute(query % args)
        total= self.mycursor.fetchone()[0] + balance # fetch one row/single record and + balance
        query="UPDATE Customer SET balance= '%s' WHERE id='%s'" # insert update query
        args=(total,id)
        self.mycursor.execute(query % args)
        self.mydb.commit()
        print(f"\tDeposite of {balance} for {id} Successful..")

    def View_balance(self,id):
        query= "SELECT balance FROM Customer WHERE id = '%s' " # insert select query
        args=(id)
        self.mycursor.execute(query % args)
        result= self.mycursor.fetchone() # fetch one record

        # check condition if result in so print id and balance or not so print not found 
        if result:
            print(f"\tBalance for {id}: {result[0]}")

        else:
            print("\tCustomer not found !!")

# using inheritance 
# sub class 
class customer2(Customer):

    # create main function
    def main_customer(self):

        # loop
        while True:
                self.Menu()
                choice=int(input("\n\tEnter Choice: "))

                if choice==1:
                    name=input("\n\tEnter Name: ")
                    password=input("\tEnter Password: ")
                    balance=input("\tEnter Balance: ")
                    self.Register(name,password,balance)

                elif choice==2:
                    name=input("\n\tEnter Name: ")
                    password=input("\tEnter Password: ")
                    self.Login(name,password)

                elif choice==3:
                    id=int(input("\n\tEnter Customer's id: "))
                    balance=float(input("\tEnter Withdrawal Amount: "))
                    self.Withdraw(id,balance)

                elif choice==4:
                    id=int(input("\n\tEnter Customer's id: "))
                    balance=float(input("\tEnter Deposite Amount: "))
                    self.Deposite(id,balance)

                elif choice==5:
                    id=int(input("\n\tEnter Customer's id: "))
                    self.View_balance(id)

                # choice program continue or not
                r_choice= input("\n\tDo You Want To Perform Press y for yes and n for no: ")
                if r_choice=="n":
                    print("\n\tThank You !!")
                    break






