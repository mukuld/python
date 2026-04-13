# Python program number 3
# Program to calculate tips to waiters
# Programmer: Mukul Dharwadkar
# Date: 18 February 2006

bill_amount = input("Please enter the amount on the bill: ")

# First calculate the tip at 15% of total bill
tip = bill_amount * 0.15
print "\n\nYou should leave $",tip, " as a tip to your server at 15%."

# Now calculate the tip at 20% of the total bill
tip = (bill_amount * 0.20)
print "\n\nYou should leave $",tip, " as a tip to your server at 20%."
