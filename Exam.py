import random

class exam:
    def __init__(self,roll):
        self.roll=roll
        self.fail=30
        self.Aplus=80

    def my_marks(self,roll):
        marks=random.randint(self.fail,self.Aplus)
        return marks

Esha=exam(95)
print(Esha.my_marks(95))