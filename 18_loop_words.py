# Python Programme Number 18
# For loop demonstration
# Programmer: Mukul Dharwadkar
# Date: 27 February 2006

word = raw_input("Enter a word: ")
count = 0

# print "\nHere's each letter in your word:"
for letter in word:
    count += 1
#    print letter
print "\nThere are", count, "letters in your word and they are:\n"
for letter in word:
    print letter

raw_input("\n\nPress enter to exit.")
