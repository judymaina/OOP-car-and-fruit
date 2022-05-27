
class Account:
    def __init__(self,name,balance,password,idnumber):
        self.name=name
        self.balance=balance
        self.password=password
        self.idnumber=idnumber
    def deposit(self,amount):
        self.amount=amount
        self.balance+=amount
        return f"Hello {self.name},your balance is {self.balance}"  
    def withdraw(self,amount):
        self.balance-=amount
        return f"Hello {self.name},your balance is {self.balance}"       
   