# MAIN FILE:

# import all modules
import Banker_file

from datetime import datetime
from Customer_file import display_details
from Customer_file import Withdraw_amount
from Customer_file import Deposite_amount
from Customer_file import View_balance

# Open file bank_file.txt 
# append in the file
f = open("Bank_File.txt","a")

# define is_valid_ac_num() function -- this use check entered ac_number length and ac_number is digits then return 
def is_valid_ac_num(ac_no):
    return ac_no.isdigit() and len(ac_no) == 9

# define is_valid_c_name() function -- this use check name is alphabetical and length is greater than 0
def is_valid_c_name(cu_name):
    return cu_name.isalpha() and len(cu_name) > 0

# define customer_details() function 
def customer_details():
    # show the current date and time in string format
    current_date_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    # use while loop and get ac_number
    while True:
        # enter account number
        ac_no = input("Enter Account Number: ")
        # check condition is_valid_ac_num true or false if true
        if is_valid_ac_num(ac_no):
            # store ac_no in num variable
            num= ac_no
            break
        # false -- print
        else:
            print("Invalid Account Number !! Enter a valid account number (only 9 digit)..")

    # use while loop and get customer name
    while True:
        # enter customer name
        cu_name = input("Enter Customer Name: ")
        # check condition is_valid_c_num true or false if true
        if is_valid_c_name(cu_name):
            # store cu_name in name variable
            name= cu_name
            break
        # false -- print    
        else:
            print("Invalid entered name !! Enter a valid name..")
    
    # enter opening balance
    op_balance= input("Enter Opening Balance: ")
    # store op_balance in o_balance variable
    o_balance = op_balance 

    return {'ac_num': num , 'c_name': name, 'balance': o_balance ,'Opening Date' : current_date_time}

# define a banker_menu() function 
def Banker_menu():
    status= True

    # use while loop
    while status:
        
        # print banker app menu
        print("\n\t\tWelcome to Banker's App")
        print("\n\t\tOperations Menu")
        print("\n\t\t1) Add Customer")
        print("\t\t2) View Customer")
        print("\t\t3) Search Customer")
        print("\t\t4) View All Customer")
        print("\t\t5) Total Amounts in Bank")
        print("\t\t6) Exit Banker App")

        # enter your operation
        choice= int(input("\n\tEnter Operation Which You Want To Perform: "))
        
        # Use ladder if-else statements and check all condition
        if choice==1:
            c_details= customer_details()
            # call add_customer function from the banker file
            b= Banker_file.Add_customer(c_details)
            # write content to the file
            f.write("\n\tCustomer Added: "+str(b))
            print("\n\tCustomer Added Succesfullyy...")
            
        elif choice==2:
            # enter account number
            num = input("\n\tEnter Account Number: ")
            # call view_customer function from the banker file
            customer= Banker_file.View_customer(num)
            # call display_details function from the customer file this show customer details
            display_details(customer)

        elif choice==3:
            # enter customer name 
            word= input("\n\tEnter Customer Name to Search: ")
            # call search_customer function from the banker file
            s=Banker_file.Search_customer(word)
            
            # use for loop
            for customer in s:
                # call display_details function from the customer file this show customer details
                display_details(customer)
           

        elif choice==4:
            # define id
            id=1
            # define blank dictionary
            all={}
            
            # call view_all_customer function from the banker file
            view_all= Banker_file.View_all_customer()
            
            # use for loop
            for customer in view_all:
                id= id+1
                all[f"{id}"] = {'c_name': customer['c_name'], 'balance': customer['balance'], 'Opening Date': customer['Opening Date']}
            
            # show all customer details
            print(all)

        elif choice==5:
            # call total_amount function from the banker file
            total= Banker_file.Total_amount()
            print(f"\n\tTotal Amount in the bank: {total}")

        elif choice==6:
            # exit from the banker
            print("\n\tExit")
            break

        else:
            # invalid choice
            print("\n\tInvalid Choice !! Please Enter Number Between (1-6)..")

        # again perform operation 
        ch= input("\n\tDo you want to perform more operations press 'y' for yes and 'n' for no: ")

        if ch=='Y' or ch=='y':
            status=True

        else:  
            print("\n\tThank You !!")
            status=False

# define a customer_menu() function 
def Customer_menu():

    status=True

    # use while loop
    while status:

        # print customer menu
        print("\n\t\tWelcome To Customer's App")
        print("\n\t\tOperations Menu")
        print("\n\t\t1)Withdraw Amount")
        print("\t\t2)Deposite Amount")
        print("\t\t3)View Balance")
        print("\t\t4)Exit Customer App")

        # enter your operation
        choice= int(input("\n\tEnter Operation Which You Want To Perform: "))

        # Use ladder if-else statements and check all condition
        if choice==1:
            # use while loop
            while True:
                # enter account number
                ac_no = input("\n\tEnter Account Number: ")
                # check condition and call is_valid_ac_num function()
                if is_valid_ac_num(ac_no):
                    num= ac_no
                    # call withdraw_amount() function from the customer file
                    Withdraw_amount(num)
                    break
                else:
                    print("\n\tInvalid Account Number !! Enter a valid account number (only 9 digit)..")

        elif choice==2:
            # use while loop
            while True:
                # enter account number
                ac_no = input("\n\tEnter Account Number: ")
                 # check condition and call is_valid_ac_num function()
                if is_valid_ac_num(ac_no):
                    num = ac_no
                    # call Deposite_amount() function from the customer file
                    Deposite_amount(num)
                    break
                else:
                    print("\n\tInvalid Account Number !! Enter a valid account number (only 9 digit)..")

        elif choice==3:
            # use while loop
            while True:
                # enter account number
                ac_no = input("\n\tEnter Account Number: ")
                # check condition and call is_valid_ac_num function()
                if is_valid_ac_num(ac_no):
                    num = ac_no
                    # call View_balance() function from the customer file
                    View_balance(num)
                    break
                else:
                    print("\n\tInvalid Account Number !! Enter a valid account number (only 9 digit)..")

        elif choice==4:
            # exit from the customer
            print("\n\tExit")
            break

        else:
            # invalid choice
            print("\n\tInvalid Choice !! Please Enter Number Between (1-4)..")

        # again perform operation 
        ch= input("\n\tDo you want to perform more operations press 'y' for yes and 'n' for no: ")

        if ch=='Y' or ch=='y':
            status=True

        else:  
            print("Thank You !!")
            status=False

# define role function 
def Role():
        # print all role
        print("\n\t-------WELCOME TO PYTHON BANK MANAGEMENT SYSTEM-------")
        print("\n\t\tSelect Your Role")
        print("\t\t1) Banker")
        print("\t\t2) Customer")
        print("\t\t3) Exit")

# define main_menu() function
def Main_menu():

    status=True
    # use while loop
    while status:
            # call role function
            Role()
            # enter your role
            choice= int(input("\n\tChoose Your Role: "))
        
            if choice==1:
                # call Banker_menu function
                Banker_menu()

            elif choice==2:
                # call Customer_menu function
                Customer_menu()

            elif choice==3:
                # print thank you..
                print("\n\tThank You..")
                break

            else:
                # invalid choice !!
                print("\n\tInvalid Choice !! Please Enter Number Between (1-3)..")

# call main_menu function
Main_menu()
# close file
f.close()