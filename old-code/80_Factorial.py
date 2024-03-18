# Python Programme Number 80
# Factorial programme to demonstrate recursion
# Programmer: Mukul Dharwadkar
# Date: 08 June 2009

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
