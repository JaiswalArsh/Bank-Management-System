#Bank Services
from database import *
import datetime

class Bank:
    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number
        
    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction "
                 f"( timedate VARCHAR(30),"
                 f"account_number INTEGER,"
                 f"remarks VARCHAR(30),"
                 f"amount INTEGER )")
        
        
    def balanceenquiry(self):
        temp=db_query(f"SELECT balance FROM customers WHERE username='{self.__username}';")
        test=temp[0][0] # type: ignore
        print(f"{self.__username} Balance is ₹{test}")
        
    def deposit(self,amount):
        temp=db_query(f"SELECT balance FROM customers WHERE username='{self.__username}';")
        test=temp[0][0]+amount # type: ignore
        db_query(f"UPDATE customers SET balance='{test}' WHERE username='{self.__username}';")
        self.balanceenquiry()
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_number}',"
                 f"'Amount Deposit',"
                 f"'{amount}'"
                 f")")
        print(f"{self.__username} Amount is Sucessfully Deposited into Your Account {self.__account_number}")
    
    def withdraw(self, amount):
        temp = db_query(
            f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        test=temp[0][0] # type: ignore
        if amount > test:
            print("Insufficient Balance")
        else:
            test = test - amount
            db_query(
                f"UPDATE customers SET balance = '{test}' WHERE username = '{self.__username}'; ")
            self.balanceenquiry()
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.__account_number}',"
                     f"'Amount Withdraw',"
                     f"'{amount}'"
                     f")")
            print(
                f"{self.__username} Amount is Sucessfully Withdraw from Your Account {self.__account_number}")
    
    def fundtransfer(self, receive, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        if amount > temp[0][0]: # type: ignore
            print("Insufficient Balance")
        else:
            temp2 = db_query(f"SELECT balance FROM customers WHERE account_number = '{receive}';")
            if temp2 == []:
                print("Account Number Does not Exists")
            else:
                test1 = temp[0][0] - amount # type: ignore
                test2 = amount + temp2[0][0] # type: ignore
                db_query(f"UPDATE customers SET balance = '{test1}' WHERE username = '{self.__username}'; ")
                db_query(f"UPDATE customers SET balance = '{test2}' WHERE account_number = '{receive}'; ")
                receiver_username = db_query(f"SELECT username FROM customers where account_number = '{receive}';")
                self.balanceenquiry()
                db_query(f"INSERT INTO {receiver_username[0][0]}_transaction VALUES (" # type: ignore
                         f"'{datetime.datetime.now()}',"
                         f"'{self.__account_number}',"
                         f"'Fund Transfer From {self.__account_number}',"
                         f"'{amount}'"
                         f")")
                db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                         f"'{datetime.datetime.now()}',"
                         f"'{self.__account_number}',"
                         f"'Fund Transfer -> {receive}',"
                         f"'{amount}'"
                         f")")
                print(f"{self.__username} Amount is Sucessfully Transaction from Your Account {self.__account_number} to {receive}")