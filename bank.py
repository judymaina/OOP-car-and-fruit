class Account:
    def __init__(self,name,idnumber):
        self.name=name
        self.balance=0
        self.transaction = 100
        self.idnumber=idnumber
        self.deposits = []
        self.withdraws = []
    def deposit(self,amount):
        if amount < 0:
            return f"Deposit must be greater than zero"
        else:
            self.balance+=amount
            self.deposits.append(f"Hello {self.name},your have deposited {amount}")
            return f"Hello {self.name},your have deposited {amount}and your new balance is {self.balance}"  
    
    def withdraw(self,amount):
        if amount<self.balance:
          return f"You have insufficient balance" 
        elif amount <=0:
            return f"Your amount should be greater zero" 
        else:
            self.balance-=amount+self.transaction
            self.withdraws.append(f"Hello {self.name}you have withdrawn{amount}")
        return f"Hello {self.name}you have withdrawn{amount}your new balance is{self.balance}"   
    def deposits_statement(self):
        for statements in self.deposits:
            print(statements)
    def withdraws_statement(self):
        for statements in self.withdraws:
            print(statements)
    def current_balance(self):
        balance=self.balance
        print(balance)