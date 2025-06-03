from register import *
from bank import *

status = False
print("Welcome To My Bank")
while True:
    try:
        register= int(input("1. SignUp\n"
                            "2. LogIn:\n"))
        if register==1 or register==2:
            if register==1:
                SignUp()
            if register==2:
                user=LogIn()
                status = True
                break
        else:
            print("Please Enter Valid Input")
    except ValueError:
        print("Invalid Input Try Again")

a = db_query(f"SELECT account_number FROM customers WHERE username = '{user}';")
account_number = a[0][0] # type: ignore
print(f"Welcome {user.capitalize()}") # type: ignore
while status:
    try:
        print("Choose Your Banking Service\n")
        facility= int(input("1. Balance Enquiry\n"
                            "2. Cash Deposit\n"
                            "3. Cash Withdraw\n"
                            "4. Funds Transfer\n"
                            "5. Exit: "))
        if facility>=1 or register<=5:
            if facility==1:
                bobj = Bank(user, account_number)
                bobj.balanceenquiry()
            elif facility==2:
                while True:
                    try:
                        amount = int(input("Enter Amount: "))
                        bobj=Bank(user,account_number)
                        bobj.deposit(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Invalid Input Try Again")
                        continue
            elif facility==3:
                while True:
                    try:
                        amount = int(input("Enter Amount: "))
                        bobj=Bank(user,account_number)
                        bobj.withdraw(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Invalid Input Try Again")
                        continue
            elif facility==4:
                while True:
                    try:
                        receiver = int(input("Enter Receiver's Account number: "))
                        amount = int(input("Enter Amount: "))
                        bobj=Bank(user,account_number)
                        bobj.fundtransfer(receiver,amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Invalid Input Try Again")
            elif facility==5:
                print("Thanks For Using Banking Services")
                status = False
        else:
            print("Please Enter Valid Input")
            continue
    except ValueError:
        print("Invalid Input Try Again")
        continue