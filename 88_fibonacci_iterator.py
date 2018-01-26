# Python Programme Number 88
# Magic Methods: Iterators
# Programmer: Mukul Dharwadkar
# Date: 15 June 2009

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):
        self.a, self.b = self.b, self.a+self.b
        return self.a
    def __iter__(self):
        return self
