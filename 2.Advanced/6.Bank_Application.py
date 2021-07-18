import sys
class Customer:
    '''Customer class with bank related operations'''
    bankname='DURGASOFT'
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    def deposit(self,amt):
        self.balance=self.balance+amt
        print("After deposit the balance:",self.balance)

    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient funds........cannot perform operations")
            sys.exit()
        self.balanc=self.balance-amt
        print("After withdraw The Balance:",self.balance)
print("Welcome to",Customer.bankname)
name=input("Enter your name:")
c=Customer(name)
while True:
    print("d-Deposit\nw-WithDraw\ne-Exit")
    option=input("choose your option")
    if option=='d' or option=='D':
        amt=float(input("Enter your amount:"))
        c.deposit(amt)
    elif option =='w' or option=='W':
        amt=float(input("Enter Amount to withdraw:"))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print("Thanks for Banking")
        sys.exit()
    else:
        print("Choose valid option")

