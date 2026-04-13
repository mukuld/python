# Python Programme Number 83
# Raising &/or passing exceptions
# Programmer: Mukul Dharwadkar
# Date: 11 June 2009

class MuffledCalculator:
    muffled = 0
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print "Division by zero is not allowed!!!"
            else:
                raise
