# BANKER FILE:

# define global customers
global customers
# define blank dictionary
customers = {}

# create a function name of add_customer()
def Add_customer(customer):
    # customer details stored in customers
    customers[customer['ac_num']] = customer
    return customers

# create a function name of view_customer()
def View_customer(ac_num):
    # get customer details
    result = customers.get(ac_num)
    return result

# create a function name of search_customer()
def Search_customer(word):
    # define blank list
    results = []

    # use loop 
    for customer in customers.values():
        # check condition use if-else
        if word.lower() in customer['c_name'].lower() or str(word).lower() in str(customer['ac_num']).lower():
            # append results in customer
            results.append(customer)
    return results

# create a function name of view_all_customer()
def View_all_customer():
    # all customer details view use values()
    return list(customers.values())

# create a function name of total_amount()
def Total_amount():
    # use of sum and values to get total amount...
    total = sum(int(customer['balance']) for customer in customers.values())
    return total



        
    
    
    
        







