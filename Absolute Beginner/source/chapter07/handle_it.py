# Handle It
# Demonstrates handling exceptions
# Michael Dawson 5/3/03

# try/except
try:
    num = float(raw_input("Enter a number: "))
except:
    print "Something went wrong!"

# specifying exception type
try:
    num = float(raw_input("\nEnter a number: "))
except(ValueError):
    print "That was not a number!"

# handle multiple exceptions
print
for value in (None, "Hi!"):
    try:
        print "Attempting to convert", value, "-->",
        print float(value)
    except(TypeError, ValueError):
        print "Something went wrong!"

print
for value in (None, "Hi!"):
    try:
        print "Attempting to convert", value, "-->",
        print float(value)
    except(TypeError):
        print "I can only convert a string or a number!"
    except(ValueError):
        print "I can only convert a string of digits!"

# get an exception's argument
try:
    num = float(raw_input("\nEnter a number: "))
except(ValueError), e:
    print "That was not a number!  Or as Python would say:\n", e

# try/except/else
try:
    num = float(raw_input("\nEnter a number: "))
except(ValueError):
    print "That was not a number!"
else:
    print "You entered the number", num     

raw_input("\n\nPress the enter key to exit.")
