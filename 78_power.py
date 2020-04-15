# Python Programme Number 78
# Story to demonstrate parameter collector
# Programmer: Mukul Dharwadkar
# Date: 20 August 2008
# Date Modified: 08 June 2009


x = input("Please enter the number you want to test: ")
y = input("Please enter the number of power you want: ")

def power(x, y, *others):
    if others:
        print "Received redundant parameters:", others
    return pow(x, y)

print power(x, y)

