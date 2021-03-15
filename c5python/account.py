class Bank_Account:
    def __init__(self,accno,name,acctype,balance):
        self.accno=accno
        self.name=name
        self.acctype=acctype
        self.balance=balance

    print("***HELLO !!! WELCOME DEAR ACCOUNT HOLDER***")

    def deposit(self):
        amount = float(input("\nEnter amount to be deposited : "))
        self.balance += amount
        print("\namount deposited :", amount)

    def withdraw(self):
        amount = float(input("\nEnter amount to be withdrawn : "))

        if self.balance >= amount:
            self.balance -= amount
            print("\nYou withdrew :", amount)
        else:
            print("\nInsufficient balance !!! ")


    def display(self):
        print("\nAccount Number : ",self.accno)
        print("Holder Name : ",self.name)
        print("Account Type : ",self.acctype)
        print("Net available Balance : ", self.balance)


account=Bank_Account(123456789,"Adwaith","Savings",5000)
account.deposit()
account.withdraw()
account.display()