#User registion SignIn and SignUp
import random
from customer import *
from bank import Bank
def SignUp():
    username = input("Create your username: ")
    temp=db_query(f"SELECT username FROM customers where username ='{username}';")
    if temp:
        print("Username already exist")
        SignUp()
    else:
        print("Username is avaliable please proceed")
        password=input("Enter Your Password: ")
        name=input("Enter Your Name: ")
        age=int(input("Enter Your age: "))
        city=input("Enter Your City: ")
        while True:
            account_number= int(random.randint(10000000,99999999))
            temp=db_query(f"SELECT account_number FROM customers WHERE account_number ='{account_number}';")
            if temp:
                continue
            else:
                print("Your account number= ",account_number)
                break
    cobj=Customer(username,password,name,age,city,account_number)
    cobj.createuser()
    bobj=Bank(username,account_number)
    bobj.create_transaction_table()
def LogIn():
    username = input("Enter Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()} Enter Password: ")
            temp = db_query(f"SELECT password FROM customers where username = '{username}';")
            test=temp[0][0] # type: ignore
            if test == password:
                print("LogIn Succesfully")
                return username
            else:
                print("Wrong Password Try Again")
                continue
    else:
        print("Enter Correct Username")
        LogIn()
    