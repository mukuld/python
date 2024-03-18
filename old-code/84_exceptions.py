# Python Programme Number 84
# Handling exceptions
# Programmer: Mukul Dharwadkar
# Date: 11 June 2009

while 1:
    try:
        x = input("First Number: ")
        y = input("Second Number: ")
        value = x/y
        print "x/y is", value
    except Exception, e:
        print "Invalid input:", e
        print "Please try again..."
    else:
        break
