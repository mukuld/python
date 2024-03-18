# Python Programme Number 17
# Computer guesses the number
# Programmer: Mukul Dharwadkar
# Date: 24 February 2006
#
# In this game, the player picks a random number between 1 and 100.
# The computer will try to guess the number. After each guess,
# the computer tells the player whether the guess is too high or too low
# or correct.

import random           # Import the module random to generate random numbers

# The next block of statements explain the game to the player
print '\tWelcome to the "Guess My Number" game'
print "\tThink of a number between 1 and 100."
print "\tI will try to guess the number in as little tries as I can."
print "\tLet's go!!!"

# Set the initial values
guess = int(raw_input("Think your number: "))
tries = 1
the_num = 0

# The loop
while (the_num != guess):
    the_num = random.randrange(100) + 1
    print "Attempt No:", tries, "-->", the_num
    tries += 1

print "\nI guessed it!!!. You number is: ", the_num
print "\nI guessed it in", tries - 1, "tries"
# End the program and congratulate the player

#raw_input("Press enter to exit.")
