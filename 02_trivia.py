# Python program number 2
# Program to introduce interactivity and simple mathematical calculation
# Programmer: Mukul Dharwadkar
# Date: 18 February 2006

name = raw_input("Hi There!! What is your name? ")
print "\nHi there, " + name.title()
print "\nLet's play a game, shall we?\n"

# Request the user to enter some details

age = int(raw_input("How old are you? "))
weight = int(raw_input("Please enter your weight in kg: "))

# Perform some meaningless calculations here
seconds = age * 365 * 24 * 60 * 60
print "Did you know that you have lived for ", seconds, " seconds?"

heart_beat = (seconds / 60) * 78
print "\nApproximately, your heart has beat for ", heart_beat, " times"

weight_pound = weight * 2.2
print "\nYour weight in pounds is ", weight_pound

# Exit
print raw_input("\nWasn't that fun to know?")
