# Python Programme Number 29
# Word Jumble Game v2.0
# Programmer: Mukul Dharwadkar
# Date: 13 March 2006
#
# In this game, the computer picks a random number from a list and jumbles it
# The player then has to un-jumble it to win. In the newer version the computer
# provides a hint for each wrong answer and limits the number of tries to 3 as
# in this case.

import random

# Create a list of words using a tuple
WORDS = ("difficult", "python", "linux", "redhat", "windows", "microsoft", "dharwadkar",
         "infosys", "philips", "yamaha", "xylophone")

HINTS1 = ("Not easy", "The internet language", "The coolest OS",
      "Maker of the coolest OS", "The most popular OS",
         "Maker of most popular OS", "The best family",
         "The best company", "The electronics giant in Europe",
      "One Motorbike manufacturer from Japan",
         "A typical instrument which comes in the alphabet express")

HINTS2 = ("Another word for 'Hard'", "It takes its name from a reptile",
          "Its mascot and inventor are found on opposite tips of the world",
          "The name also means a coloured head gear",
          "Its the most popular, but not the most secure.",
          "The rise of the company is legendary in software industry",
          "The family hails from Karnataka", "The company is HQed in Bangalore",
          "The company is HQed in the Netherlands",
          "They also manufacture musical instruments",
          "It start with the 24th letter of the alphabet")

# Pick random index to choose the word from the above tuple
index = len(random.choice(WORDS))

word = WORDS[index]

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
    if chances == 2:
        print "Hint", chances-1, ":", HINTS1[index]
    guess = raw_input("\nYour Guess: ")
    guess = guess.lower()
    if guess != correct and chances == 2:
        print "Hint", chances, ":", HINTS2[index]
    chances -= 1

score = (10, 5, 2)

if guess == correct and chances == 2:
    print "That's it. You have guessed the word correctly. You scored", score[0],\
          "points\n"
elif guess == correct and chances == 1:
    print "That's it. You have guessed the word correctly. You scored only", score[1],\
          "points\n"
elif guess == correct and chances == 0:
    print "That's it. You have guessed the word correctly. You scored only", score[2],\
          "points\n"
else:
    print "\nYou lose. Please try again later."

print "Thanks for playing. That was fun."

raw_input("\n\nPress enter to exit.")
