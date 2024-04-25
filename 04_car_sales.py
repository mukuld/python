# Python Program Number 4
# Program to calculate sale price of the car based on given price
# Programmer: Mukul Dharwadkar
# Date: 22 February 2006

print "\tWelcome to Mukul Dharwadkar's used car shop"
print "\a\a"

base_price = input("\nWhat is the price of the car: ")

tax = base_price * 0.0825
license_plate = base_price * 0.02
commission = 500
misc_charge = 250

sale_price = base_price + tax + license_plate + commission + misc_charge

print "\nThe total price of the car after all extras is: ", sale_price
