# Python Programme Number 22
# No Vowels: Demonstrate immutability and creation of strings
# Programmer: Mukul Dharwadkar
# Date: 6 March 2006

message = raw_input("Enter your message: ")
new_message = ""
VOWELS = "aeiou"

print
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
#        print "A message is generated for you:", new_message

print "\nThe message without vowels is: ", new_message

#raw_input("Press Enter to exit.")
