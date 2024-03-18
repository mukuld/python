# Python Programme Number 21
# Introduction to indexing
# Programmer: Mukul Dharwadkar
# Date: 5 March 2006

import random

word = raw_input("Enter any word: ")
print "The word you entered is: ", word, "\n"

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low, high)
    print "Word[", position, "]\t", word[position]

raw_input("Press enter to exit.")
