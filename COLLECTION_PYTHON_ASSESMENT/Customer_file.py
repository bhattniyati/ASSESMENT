# CUSTOMER FILE:

# import banker file
import Banker_file

# create a function name of withdraw_amount() 
def Withdraw_amount(ac_num):
    # define empty dictionary
    customers = {}
    # Open file and read from file
    with open('Bank_File.txt', 'r') as file:
        for line in file:
            # convert the string to a dictionary
            customer_data = eval(line)
            # Update the customers dictionary with the data from the file
            customers.update(customer_data)
            

    # Check if the account number exists in the data
    if ac_num in customers:
        # Get the account details through account number
        ac_no = customers[ac_num]
        # Print account holder name and available balance
        print("Account Holder Name:", ac_no['Customer Name'])
        print("Available Balance:", ac_no['Balance'])


        # enter the withdrawal amount
        withdraw_am = int(input("Enter Withdraw Amount: "))

        # Check if the balance is sufficient for withdrawal
        if int(ac_no['Balance']) > int(withdraw_am):
            # Deduct the withdrawal amount from the balance
            ac_no['Balance'] = int(ac_no['Balance']) - int(withdraw_am)
            print("Withdrawal Successful...")
            print("Balance in your account: ",ac_no['Balance'])
        else:
            print("Error: Balance not available in your account!")

         # Write data into the file
        with open('Bank_File.txt', 'w') as file:
            # use loop-- Write each customer's details in the dictionary format
            for acc_num, customer_details in customers.items():
                # write data
                file.write(str({acc_num: customer_details}) + '\n')
    else:
        print("Error: Account does not exist!")
    

# create a function name of deposite_amount()
def Deposite_amount(ac_num):
    # define empty dictionary
    customers = {}
    # Open file and read from file
    with open('Bank_File.txt', 'r') as file:
        for line in file:
            # convert the string to a dictionary
            customer_data = eval(line)
            # Update the customers dictionary with the data from the file
            customers.update(customer_data)

    # Check if the account number exists in the data
    if ac_num in customers:
        # Get the account details through account number
        ac_no = customers[ac_num]
        # Print account holder name and available balance
        print("Account Holder Name:", ac_no['Customer Name'])
        print("Available Balance:", ac_no['Balance'])
        # enter amount
        deposite_am = input("Enter Deposite Amount: ")
        # current balance in plus deposite amount
        ac_no['Balance'] = int(ac_no['Balance']) + int(deposite_am)
        print("Deposite Successfully...")
        # check amount after deposite
        print("Balance in your account : ",ac_no['Balance'])

         # Write data into the file
        with open('Bank_File.txt', 'w') as file:
           # use loop-- Write each customer's details in the dictionary format
            for acc_num, customer_details in customers.items():
                # write data
                file.write(str({acc_num: customer_details}) + '\n')
        
    else:
        print("Error: Account does not exist!!")

# create a function name of view_balance()
def View_balance(ac_num):

    data={}
    # Open file and read from file
    with open('Bank_File.txt', 'r') as file:
        # read file and convert string into dictionary using eval store into data
        for line in file:
            data.update(eval(line))

    # Check if the account number exists in the data
    if ac_num in data:
        # Get the account details through account number
        ac_no = data[ac_num]
        # print details
        print("Account Number: ",ac_num)
        print("Account Holder Name: ",ac_no['Customer Name'])
        print("Available Balance in Your Account: ",ac_no['Balance'])
    else:
        print('Account does not exist !!')




