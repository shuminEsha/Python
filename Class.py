class bank:
    def __init__(self,account_balance):
        self.balance=account_balance #instance 
        self.min_withdraw=100
        self.max_withdraw=100000


    def get_balance(self):
        return self.balance
    
    def deposite(self,amount):
        if amount >0 :
            self.balance+=amount
            return f'Your current balance is {self.balance}'
        
    def withdraw(self,amount):
        if amount<self.min_withdraw:
            return f'You can not withdraw below {self.min_withdraw}'
        elif amount>self.max_withdraw:
            return f'You can not withdraw more than {self.max_withdraw}'
        else:
            self.balance-=amount
            return f'Your bank account has {self.balance} money '
            

Esha=bank(20000)
print(Esha.deposite(1000))
print(Esha.withdraw(2000))
