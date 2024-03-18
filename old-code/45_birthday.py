# Python Programme Number 45
# Birthday Wishes: Demonstrates keyword arguments and default parameter values
# Programmer: Mukul Dharwadkar
# Date: 31 March 2006

# Postional Parameters
def birthday1(name, age):
    print "Happy Birthday,", name, "!", " I hear you are", age, "today.\n"

# Parameters with default values
def birthday2(name = "Jayant", age = 2):
    print "Happy Birthday,", name, "!", "I hear you are", age, "today.\n"


birthday1("Jayant", 2)
birthday1(2, "Jayant")
birthday1(name = "Jayant", age = 2)
birthday1(age = 2, name = "Jayant")

birthday2()
birthday2(name = "Shital")
birthday2(age = 29)
birthday2(name = "Shital", age = 29)
birthday2("Shital", 29)

raw_input("\nPress enter to exit.")
