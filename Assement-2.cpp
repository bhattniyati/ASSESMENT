#include<iostream>
#include<ctime>
using namespace std;

class ATM{
	
	public:
	void display();
	ATM()
	{
		// Current Date and Time
		time_t now = time(0);
		char* date_time = ctime(&now);
		
		cout<<endl<<"===========================WELCOME TO ATM===========================";
		cout<<endl<<endl<<"                         ------------------                         ";
		cout<<endl<<endl<<"     Current Date And Time: "<<date_time;
		cout<<endl<<endl<<"                         ------------------                         ";
		cout<<endl<<endl<<"====================================================================";
	}	
};
void ATM::display()
{
	int p_code,choice,ch;
		cout<<endl<<endl<<"  Press 1 and Then Press Enter to Access Youe Account Via Pin Number";
		cout<<endl<<endl<<"                                   or                                ";
		cout<<endl<<endl<<"  Press 0 and Press Enter to Get Help.\n\n";
		cin>>choice;
		
		if(ch==1)
		{
			cout<<endl<<"===========================ATM ACCOUNT ACCESS===========================";
			cout<<"\n \n Enter Your Acc Pin Access Number! [Only One Attempt is Allowed]";
			cout<<"\n \n=========================================================================\n";
			cin>>p_code;
			
			if(p_code==12345)
			{
				cout<<endl<<"===========================ATM MAIN MENU SCREEN==========================="<<endl<<endl;
	            cout<<endl<<"\t\tEnter [1] To Depostie Cash \n";
	            cout<<endl<<"\t\tEnter [2] To Withdraw Cash \n";
	            cout<<endl<<"\t\tEnter [3] To Balance Inquiry \n";
	            cout<<endl<<"\t\tEnter [0] To Exit ATM \n";
	            cout<<endl<<"\t\tPLEASE ENTER A SELECTION AND PRESS RETURN KEY: \n";
	            cin>>choice;
	            
	            switch(choice)
				{       
					case 1:
						int dep_amt,wit_amt,ac_no,balance;
						string name,add,loc;
						
						cout<<endl<<endl<<"===========================ATM ACCOUNT DEPOSITE SYSTEM===========================";
			            cout<<endl<<endl<<"\tThe Names Of the Account Holders are: ";
			            cin>>name;
			            cout<<endl<<endl<<"\tThe Account Holder's address is: ";
			            cin>>add;
			            cout<<endl<<endl<<"\tThe Branch Location is: ";
			            cin>>loc;
			            cout<<endl<<endl<<"\tAccount Number: ";
			            cin>>ac_no;
			            cout<<endl<<endl<<"\tPresent Available Balance is: Rs.";
			            cin>>balance;
			            cout<<endl<<endl<<"\tEnter the Amount to be Deposited Rs. ";
			            cin>>dep_amt;
			            cout<<endl<<endl<<"\tYour New available Balance Amount is Rs.";
						cout<<endl<<endl<<"\tYour New Balance is RS. "<<balance+dep_amt;
			            cout<<endl<<endl<<"\t\tThank You!! ";
			            break;
	
		       		case 2:
			        	int ac_num;
						string Name,address,location;
						
			        	cout<<endl<<endl<<"===========================ATM ACCOUNT WITHDRAWAL SYSTEM===========================";
			             cout<<endl<<endl<<"\tThe Names Of the Account Holders are: ";
			             cin>>name;
			             cout<<endl<<endl<<"\tThe Account Holder's address is: ";
			             cin>>address;
			             cout<<endl<<endl<<"\tThe Branch Location is: ";
			             cin>>location;
			             cout<<endl<<endl<<"\tAccount Number: ";
			             cin>>ac_num;
			             cout<<endl<<endl<<"\tInsufficient Available Balance in your account. ";
			             cout<<endl<<endl<<"\t\tSorry  !!";
			             break;

				}
			}
			else
			{
				cout<<endl<<"===========================THANK YOU===========================";
				cout<<endl<<endl<<"You Had made your attempt which failed!!! No More Attempts Allowed!! Sorryy !!";
				cout<<endl<<endl<<"======================================================";
			}
		}
		else 
		{
			cout<<endl<<endl<<"===========================ATM ACCOUNT STATUS===========================";
			cout<<"\n \n \tYou must have the correct pin number to access this account. \n See your bank representative for assistance during bank opening hours \n Thanks for, your choice today !!";
			cout<<"\n \n========================================================================";
		}		
}

int main()
{
	ATM obj;
	obj.display();
	
	return 0;
}
