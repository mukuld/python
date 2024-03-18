# Python Programme Number 27
# Learn to Count: Implementing indexes
# Programmer: Mukul Dharwadkar
# Date: 8 March 2006

print "Hello and welcome to the counter."
print "This program will help you count from any number to any number",
print "with any number of increment."
print "Are you ready for some fun?"

begin = int(raw_input("Please enter the starting number: "))
end = int(raw_input("Please enter the ending number: "))
if begin >= end:
    print "Uh-Oh, This is not a valid entry."
    print "The ending number must be greater than the starting number."
    end = int(raw_input("Please enter the ending number: "))

step = int(raw_input("Please enter the increment in which you want to count: "))
if step >= ((end - begin)/2) or step == 0:
    print "This is an invalid entry."
    step = int(raw_input("Please enter the increment in which you want to count: "))

# Now we will start counting
for i in range(begin, end, step):
    print i

raw_input("Press enter to exit.")
