import pymysql

# import modules
import banker 
import customer

# connect database
mydb= pymysql.connect(host="localhost",user="root",password="",database="Banking_Application")
mycursor= mydb.cursor()


# create object of base class from banker file 
b=banker.banker2()
# create object of base class from customer file
c=customer.customer2()

# loop
while True:
        
        mainmenu="""
            Main System
            1). Banker
            2). Customer
            3). Exit
        """

        print(mainmenu)
        choice = int(input("\n\tEnter Choice: "))

        if choice==1:
            b.main_banker() # call function of banker file through object 

        elif choice==2:
            c.main_customer() # call function of customer file through object 
            
        else:
            print("\n\tExit")
            break
        
        # choice program continue or not 
        r_choice= input("\n\tDo You Want To Perform Main System Press y for yes and n for no: ")
        if r_choice=="n":
            print("\n\tThank You !!")
            break