# Python Programme Number 5
# Craps roller using random numbers
# Programmer: Mukul Dharwadkar
# Date: 22 February 2006

import random

# Generate random number from 1 to 6
die1 = random.randrange(6) + 1
die2 = random.randrange(6) + 1

total = die1 + die2

print "You rolled a", die1, "and a", die2, "for a total of", total

#raw_input("\nPress the enter key to exit")
