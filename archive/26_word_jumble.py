# Python Programme Number 26
# Word Jumble Game
# Programmer: MukulDharwadkar
# Date: 8 March 2006
#
# In this game, the computer picks a random number from a list and jumbles it
# The player then has to un-jumble it to win

import random

# Create a list of words using a tuple
WORDS = ("difficult", "python", "linux", "redhat", "windows", "microsoft", "dharwadkar",
         "infosys", "philips", "yamaha", "xylophone", "apple")

# Pick one word randomly from the above tuple
word = random.choice(WORDS)

# Create a variable to test whether the player makes a correct guess
correct = word

# Create a jumbled word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[position + 1:]

# Start the game
print \
      """


          Welcome to the Word Jumble!!!

        Unscramble the letters to guess the original word.
        (Press enter at prompt to exit.)

    """

print "The jumble is: ", jumble
print "You have only 3 chances to guess."

# Get the players guess
guess = raw_input("\nYour Guess: ")
guess = guess.lower()
chances = 2
while (guess != correct) and (guess != "") and chances:
    print "Sorry, that's not it."
    guess = raw_input("\nYour Guess: ")
    guess = guess.lower()
    chances -= 1

if guess == correct:
    print "That's it. You have guessed the word correctly.\n"
else:
    print "\nYou lose. Please try again later."

print "Thanks for playing. That was fun."

raw_input("\n\nPress enter to exit.")
    
