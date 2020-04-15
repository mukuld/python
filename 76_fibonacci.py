# Python programme number 75
# Fibonacci Series
# Programmer: Mukul Dharwadkar
# Date: 15 August 2008

fibs = [0, 1]

num = input("How many Fibonacci numbers do you want?: ")

for i in range(num-2):
    fibs.append(fibs[-2] + fibs[-1])

print fibs
