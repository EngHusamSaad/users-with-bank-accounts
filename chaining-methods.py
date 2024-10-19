class user:
    def __init__(self,name, email):
        self.name=name
        self.email=email
        self.account_balance=0

    def make_deposit(self, amount):
        self.account_balance+=amount
        return self
        

    def make_withdrawal(self, amount):
        if(self.account_balance<=0):
            print("No Credit !")
        else:
             self.account_balance-=amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self


    def transfer_money(self,reciver,amount):
        self.account_balance-=amount
        reciver.account_balance+=amount
        return self
         
    


husam=user("husam","husam@gmail.com")
ahmad=user("ahmad","ahmad@gmail.com")
said=user("said","said@gmail.com")

husam.make_deposit(10).make_withdrawal(1).display_user_balance()

ahmad.make_deposit(10).make_withdrawal(2).display_user_balance()


said.make_deposit(10).make_withdrawal(3).display_user_balance()


husam.display_user_balance()
said.display_user_balance()

husam.transfer_money(said,2) #Husam transfer to said 2 

husam.display_user_balance()
said.display_user_balance()









