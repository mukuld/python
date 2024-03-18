# Python Programme Number 70
# Sequence Membership demonstration programme
# Programmer: Mukul Dharwadkar
# Date: 6th December 2006

# Check a user name and PIN code

database = [
    ["mukul", "1234"],
    ["shital", "2345"],
    ["jayant", "3456"],
    ["nandini", "4567"]
    ]
user_name = raw_input("Enter your User name: ")
pin = raw_input("Enter you PIN Code: ")

if [user_name.lower(), pin] in database:
    print "Access Granted"
else:
    print "Access Denied"
