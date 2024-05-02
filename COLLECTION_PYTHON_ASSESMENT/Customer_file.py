# CUSTOMER FILE:

# import banker file
import Banker_file

# create a function name of display_details()
def display_details(customer):

    if customer:
        print("Customer Details: ")
        print(f"Customer Name: {customer['c_name']}")
        print(f"Customer Balance: {customer['balance']}")
    else:
        print("Customer Not Found !!")


# create a function name of withdraw_amount() 
def Withdraw_amount(ac_num):
    # get customer details in banker_file when entered account number.
    result= Banker_file.customers.get(ac_num)

    # Use if-else statement and check condition customer or not !
    if result:
        # print account holder name and balance
        print("Account Holder Name: ",result['c_name'])
        print("Available Balance: ",result['balance'])
        # enter amount
        withdraw_am = input("Enter Withdraw Amount: ")
        # then check condition balance is greater than withdraw amount
        if int(result['balance']) > int(withdraw_am):
            # if true then current balance in minus withdraw amount
            result['balance'] = int(result['balance']) - int(withdraw_am)
            print("Withdrawal Successfully...")
            print("Balance in your account : ",result['balance'])
        # else false -- print 
        else:
            print("Error Amount not available in your account !!")
    # else not -- print
    else:
        print("Account does not exist!!")

# create a function name of deposite_amount()
def Deposite_amount(ac_num):
    # get customer details in banker_file when entered account number.
    result= Banker_file.customers.get(ac_num)

    # Use if-else statement and check condition customer or not !
    if result:
        # print account holder name and balance
        print("Account Holder Name: ",result['c_name'])
        print("Available Balance: ",result['balance'])
        # enter amount
        deposite_am = input("Enter Deposite Amount: ")
        # current balance in plus deposite amount
        result['balance'] = int(result['balance']) + int(deposite_am)
        print("Deposite Successfully...")
        # check amount after deposite
        print("Balance in your account : ",result['balance'])
        
    else:
        print("Account does not exist!!")

# create a function name of view_balance()
def View_balance(ac_num):
    # get customer details in banker_file when entered account number.
    result=Banker_file.customers.get(ac_num)
    # Use if-else statement and check condition customer or not !
    if result:
        # print details
        print("Account Holder Name: ",result['c_name'])
        print("Account Number: ",result['ac_num'])
        print("Available Balance in Your Account: ",result['balance'])
    else:
        print('Account does not exist !!')




