# BANKER FILE:

# import date time module
from datetime import datetime

# define blank dictionary
customers = {}

# create a function name of add_customer()
def Add_customer():
    # Take input from the user
    ac_num = input("\n\tEnter Account Number: ")
    c_name = input("\tEnter Customer Name: ")
    balance = float(input("\tEnter Balance: "))  # Convert input to float for balance
    current_date_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S") # show the current date and time in string format

    customers = {
        ac_num: {
            'Customer Name': c_name,
            'Balance': balance,
            'Opening Date': current_date_time
        }
    }
    # Open the file and append data
    with open("Bank_File.txt",'a') as file:
        # write in customers empty dictionary
        file.write(f"{customers}\n")
    
    print("\t\nCustomer details added successfully.")

# create a function name of view_customer()
def View_customer(ac_num):
    # Open the file and read
    with open('Bank_File.txt', 'r') as file:
        # use loop
        for line in file:
            # Check if the account number is present in the line
            if ac_num in line:
                print("\n\tCustomer Details", line)
                return  # Exit the function after printing the details
    
    # If the loop completes without finding the account number, print a message
    print("\n\tAccount not found in the file.")


# create a function name of search_customer()
def Search_customer(c_name):
    # Open the file and read each line
    with open('Bank_File.txt', 'r') as file:
        # use loop
        for line in file:
            # Convert the line to a dictionary using eval
            customer_data = eval(line)
            
            # use loop through each customer in the dictionary
            for ac_number, customer_details in customer_data.items():
                #get customer name from the details dictionary 
                customer_name = customer_details.get('Customer Name').lower()
                
                cu_name = c_name.lower()

                # Check if the customer names match
                if customer_name == cu_name:
                    # Print the account holder name, account number, and available balance
                    print("\n\tAccount Number:", ac_number)
                    print("\tAccount Holder Name:", customer_details['Customer Name'])
                    print("\tAvailable Balance:", customer_details['Balance'])
                    return  
             
    #  customer is not found
    print("\n\tError: Account does not exist!")

# create a function name of view_all_customer()
def View_all_customer():
   # Open the file and read file 
   with open('Bank_File.txt', 'r') as file:
        # use readlines to read all lines in the file
        lines= file.readlines()
        print("\n\tView All Customer Details: ")
        # use loop
        for customer in lines:
            print("\n\t",customer)
    

# create a function name of total_amount()
def Total_amount():
    total = 0  # define total is 0

    # Open the file and read
    with open('Bank_File.txt', 'r') as file:
        # Read all lines in the file
        lines = file.readlines()

        # use for loop
        for line in lines:
            # Convert the line to a dictionary
            data = eval(line)
            
            #  use loop each customers data in the dictionary and add balance to the total
            for customer_data in data.values():
                total += customer_data['Balance']
    
    # Print the total balance
    print(f"\n\tTotal balance in the bank: {total}")
