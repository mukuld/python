# Python Programme Number 36
# The Hangman Game
# Programmer: Mukul Dharwadkar
# Date: 19 March 2006

import random

HANGMAN = (
    """
    ----
   |    |
   |
   |
   |
   |
   |
   |
   |
-------
""",
        """
    ----
   |    |
   |    0
   |
   |
   |
   |
   |
   |
-------
""",
    """
    ----
   |    |
   |    0
   |   -+-
   |
   |
   |
   |
   |
-------
""",
        """
    ----
   |    |
   |    0
   |  /-+-
   |
   |
   |
   |
   |
-------
""",
        """
    ----
   |    |
   |    0 
   |  /-+-/
   |
   |
   |
   |
   |
-------
""",
        """
    ----
   |    |
   |    0
   |  /-+-/
   |    |
   |
   |
   |
   |
-------
""",
    """
    ----
   |    |
   |    0
   |  /-+-/
   |    |
   |    |
   |    |
   |    |
   |
-------
""",
    """
    ----
   |    |
   |    0
   |  /-+-/
   |    |
   |    |
   |   | |
   |   | |
   |
-------
""",)

# The following constant sets the number of tries
# based on the number of characters in the word
MAX_WRONG = len(HANGMAN) - 1

# The list of words
WORDS = ("OVERUSED", "SHITAL", "MUKUL", "JAYANT", "INDIA", "CLAM", "GUAM", "PUCK",
         "COFFEE", "HOUSE", "LAPTOP", "COMPUTER", "HACKER", "NANDINI")

# Define and initialise variables
word = random.choice(WORDS)

# The next variable displays the letters guessed by the player and also
# provides important hint as to how many letter are there in the word.

so_far = "*" * len(word)

wrong = 0

# Create a list to store the letters guessed by the player
used = []

# Greet the player
print \
      """
      Welcome to Hangman.
      Good luck!!
      Your word power and guessing skills
      can save a life or two today.
      """
while wrong < MAX_WRONG and so_far != word:
    print HANGMAN[wrong]
    print "\nYou've used the following letters: \n", used
    print "\nSo far, the word is: \n", so_far

    guess = raw_input("\nEnter your guess: ")
    guess = guess.upper()

    while guess in used:
        print "You've already guessed the letter:", guess
        guess = raw_input("Enter you guess: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print "\nYes!", guess, "is in the word!"

        # Create a new variable to display the letters guessed.
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]

        so_far = new
    else:
        print "\nSorry,", guess, "isn't in the word."
        wrong += 1

if wrong == MAX_WRONG:
    print HANGMAN[wrong]
    print """
    Oh Dear!! I guess your word power isn't strong enough to save a life.
    The poor guy has just been hanged.
    Better luck next time.
    """
else:
    print "You've guessed it."

print "The word was: ", word

print"\nPress enter to exit."
