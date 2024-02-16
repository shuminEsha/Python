class balance:
    def __init__(self,account_balance):
        self.balance=account_balance
        self.min_withdraw=100
        self.max_withdraw=100000


    def get_balance(self):
        return self.balance
    
    def deposite(self,amount):
        if amount >0 :
            self.balance+=amount
            