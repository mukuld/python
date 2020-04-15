# Python Programme Number 44
# Fibonacci Series
# Programmer: Mukul Dharwadkar
# Date: 27 March 2006

limit = input("Please enter the limit till which you want to create the series: ")

num1 = 1
num2 = 1
print num1
print num2

while num2 < limit:
    num3 = num1 + num2
    ratio = num2 * 1.0 / num1
    print num3
    ## print "Ratio of successive number:", ratio
    num1 = num2
    num2 = num3

raw_input("Press enter to exit")
