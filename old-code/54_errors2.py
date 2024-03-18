# Python Programme Number 54
# Handling mutliple errors
# Programmer: Mukul Dharwadkar
# Date: 23 June 2006

try:
    num = float(raw_input("Enter a number: "))
except(ValueError):
        print "That was not a number"
else:
    print "Thanks for entering the number ", num

raw_input("\n\nPress Enter to exit. ")
