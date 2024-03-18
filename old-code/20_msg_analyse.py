# Python Programme Number 20
# Message analyser to demonstrate len() funtion
# Programmer: Mukul Dharwadkar
# Date: 5 March 2006

message = raw_input("Enter a message for the world: ")

print "\nYour message is ", len(message), "characters long."

print "\nThe most common letter in English Language, 'e',",
if "e" in message:
    print "is in your message."
else:
    print "is not in your message."

raw_input("Press enter to exit.")
