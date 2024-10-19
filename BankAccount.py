class BankAccount:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.account_balance=0
        self.interestrate=.01


    def deposit(self, amount):
        self.account_balance+=amount
        return self

    def withdraw(self, amount):
        if(self.account_balance<=0):
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance-=5
        else:
             self.account_balance-=amount
        return self

    def display_account_info(self):
        print("Balance:$",self.account_balance)
        return self
    
    def yield_interest(self):
        self.account_balance+=self.account_balance*self.interestrate
        return self
    

    # To the first account, make 3 deposits and 1 withdrawal, 
    # then yield interest and display the account's info all in one line of code (i.e. chaining)

ahmad=BankAccount("ahmad","Jenin")
samer=BankAccount("samer","Hebron")

ahmad.deposit(3).withdraw(1).yield_interest().display_account_info()

samer.deposit(2).withdraw(4).yield_interest().display_account_info()







    
