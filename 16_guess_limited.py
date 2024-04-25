# Python Programme Number 16
# Guess my number game - Modified
# Programmer: Mukul Dharwadkar
# Date: 24 February 2006
#
# In this game, the computer picks a random number between 1 and 100.
# The player of the game has to guess the number. After each guess,
# the computer tells the player whether the guess is too high or too low
# or correct. If the player fails to guess in 10 tries, the game ends
# and the player loses.

import random           # Import the module random to generate random numbers

# The next block of statements explain the game to the player
print '\tWelcome to the "Guess My Number" game'
print "\tI'm thinking of a number between 1 and 100."
print "\tTry to guess the number in as little tries as you can."
print "\tAll the best!!!"

# Set the initial values
the_num = random.randrange(100) + 1
guess = input("Take a guess: ")
tries = 1

# The loop
while (guess != the_num) and (tries <= 10):
    if (guess < the_num):
        print "Your guess is too low. Increase the guess..."
    else:
        print "Your guess is too high. Lower the guess..."

    guess = int(raw_input("Take a guess: "))
    tries += 1

if (tries > 10):
    print "You lost. You could not guess the number in", tries - 1, "tries"
    print "The number was", the_num
    print "Game Over!!!"
else:
    print "You guessed it!! The number was", guess
    print "And it took you only", tries, "tries!\n"
        
# End the program and congratulate the player

raw_input("Press enter to exit.")
