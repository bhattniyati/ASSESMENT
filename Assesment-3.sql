create database Information;

use Information;

create table Bank
(
	Branch_id int primary key,
    Branch_name varchar(30),
	Branch_city varchar(20)
);

create table Loan_table
(
	Loan_no int,
	Loan_amount int,
    Loan_type varchar(20),
    Branch_id int,
    account_holders_id int,
    foreign key (Branch_id) references Bank(Branch_id),
    foreign key (account_holders_id) references Account_holder(account_holders_id)
);

create table Account_holder
(
	account_holders_id int primary key,
    account_holders_name varchar(20),
    City text,
    Contact varchar(10),
    Date_of_account_created date,
    Account_status varchar(10),
    Account_type varchar(20),
    Balance int
);

alter table Loan_table
modify Loan_no int primary key;

insert into Bank(Branch_id,Branch_name,Branch_city) values
(101,"BOB","Ahmedabad"),
(102,"SBI","Surat"),
(103,"Axis Bank","Gandhinagar"),
(104,"SBI","Rajkot"),
(105,"Kotak Mahindra Bank","Ahmedabad");

select * from Bank;

insert into Loan_table(Loan_no,Loan_amount,Loan_type,Branch_id,account_holders_id) values
(10,100000,"Student Loan",101,1),
(20,1000000,"Home Equity Loan",102,2),
(30,500000,"Auto Loan",102,2),
(40,600000,"Personal Loan",103,3),
(50,500000,"Small Business Loan",104,3);

select * from Loan_table;

insert into Account_holder(account_holders_id,account_holders_name,City,Contact,Date_of_account_created,Account_status,Account_type,Balance) values
(1,"Shyam","Ahmedabad","9506510346","2013-05-15","Active","Savings",50000),
(2,"Ram","Surat","9865243687","2013-04-14","Terminated","Current",60000),
(3,"Riya","Rajkot","9998676647","2013-05-02","Active","Fixed Deposite",80000),
(4,"Ruchi","Ahmedabad","6359452317","2013-05-15","Active","Recurring Deposite",30000),
(5,"Kajal","Surat","9106523346","2013-05-20","Terminated","Savings",80000);

select * from Account_holder;

-- Consider an example where there’s an account holder table where we are
-- doing an intra bank transfer i.e. a person holding account A is trying to transfer $100 to account B.
-- for this you have to make a transaction in sql which can transfer fund from account A to B
-- Make sure after the transaction the account information 
-- have to be updated for both the credit account and the debited account

	
	start transaction;
	update Account_Holder set balance = balance - 100 where account_holders_id = 1;
	update Account_Holder set balance = balance + 100 where account_holders_id = 2;
	commit;


-- Also fetch the details of the account holder who are related from the same city 

	select * from Account_holder
	where city in("Surat","Ahmedabad");
    
-- Write a query to fetch account number and account holder name, whose
-- accounts were created after 15th of any month

	select account_holders_id, account_holders_name, Date_of_account_created
    from Account_holder
    where day(Date_of_account_created)>15;
    
-- Write a query to display the city name and count the branches in that city.
-- Give the count of branches an alias name of Count_Branch.

	select Branch_city as Count_branch
    from Bank
    group by branch_city;

-- Write a query to display the account holder’s id, account holder’s name,
-- branch id, and loan amount for people who have taken loans. (NOTE : use
-- sql join concept to solve the query)

	select A.account_holders_id,A.account_holders_name, L.Branch_id,L.Loan_amount
    from Account_holder as A
    join Loan_table as L on A.account_holders_id = L.account_holders_id;

