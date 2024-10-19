class user:
    def __init__(self,name, email):
        self.name=name
        self.email=email
        self.account=BankAccount(balance=0,interestrate=.01) #first task

    def make_deposit(self, amount):
        self.account.deposit(amount)   #Second Task
        return self
        

    def make_withdrawal(self, amount):  #Third Task
        if(self.account<=0):
            print("No Credit !")
        else:
             self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print("self.account")
        print(self.account)     #forth Task
        return self


    def transfer_money(self,reciver,amount):
        self.account_balance-=amount
        reciver.account_balance+=amount
        return self
    
class BankAccount:
    def __init__(self,balance,interestrate):
        self.account=balance
        self.interestrate=interestrate


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
    
         
    


husam=user("husam","husam@gmail.com")
ahmad=user("ahmad","ahmad@gmail.com")
said=user("said","said@gmail.com")

husam.display_user_balance








