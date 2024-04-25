# Python Programme Number 81
# Another implementation of recursive functions to calculate power of numbers
# Programmer: Mukul Dharwadkar
# Date: 08 June 2009


def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)
