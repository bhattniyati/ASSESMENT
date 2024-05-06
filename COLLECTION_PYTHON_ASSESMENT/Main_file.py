# MAIN FILE:

# import all modules
import Banker_file
from Customer_file import Withdraw_amount
from Customer_file import Deposite_amount
from Customer_file import View_balance


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
            # call Add_customer function from the banker file
            Banker_file.Add_customer()
            
        elif choice==2: 
            # enter account numbers
            ac_num= input("\n\tEnter Account Number: ")
            # call view_customer function from the banker file
            Banker_file.View_customer(ac_num)

        elif choice==3:
            # enter customer name 
            c_name = input("\n\tEnter Customer Name to Search: ")
            # call search_customer function from the banker file
            Banker_file.Search_customer(c_name)
            

        elif choice==4:
            # call view_all_customer function from the banker file
            Banker_file.View_all_customer()
            
        elif choice==5:
            # call total_amount function from the banker file
            Banker_file.Total_amount()
            

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
            # enter account number
            ac_no = input("\n\tEnter Account Number: ") 
            # call Withdraw_amount() function from the customer file
            Withdraw_amount(ac_no)  
                  
        elif choice==2:
            # enter account number
            ac_no = input("\n\tEnter Account Number: ")      
            # call Deposite_amount() function from the customer file
            Deposite_amount(ac_no)
                  
        elif choice==3:
            # enter account number
            ac_no = input("\n\tEnter Account Number: ")
            # call View_balance() function from the customer file
            View_balance(ac_no)      

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
