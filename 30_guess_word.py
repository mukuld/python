# Python Programme Number 30
# Guess the word game: Implementation of tuples and in
# Programmer: Mukul Dharwadkar
# Date: 14 March 2006

import random

# Create a list of words
WORDS = ("sheetal", "delllaptop", "jurassic", "sholay",
         "keyboard", "synthesizer", "flatpanel", "refrigerator",
         "workhorse")

# Choose a random word from the list defined above
word = random.choice(WORDS)

# Assign the chosen word to a variable so that it can be used later
correct = word
so_far = "*" * len(word)

# Start the game.
print """
            Hello and Welcome to 'Guess my number' game

        I will choose a random word from what I know and you will get
        five chances to ask me if a letter exists in the word. After that
        you have to guess that word. The less questions you ask, the more
        you score.

        Best of luck!!!
        """
print "The word that I have chosen is", len(word), "characters long."

chances = 5

while chances:
    print "\nSo far the word is:\n", so_far
    letter = raw_input("Which letter do you choose: ")
    if letter in word:
        print "The letter exists in the word. Good work"
        new = ""
        for i in range(len(word)):
            if letter == word[i]:
                new += letter
            else:
                new += so_far[i]
        so_far = new
    else:
        print "Bad luck. This letter does not exist in this word."
    chances -= 1

print "Please take a guess."
guess = raw_input("Your guess: ")
guess = guess.lower()

if guess == correct:
    print "Congratulations, you have guessed the word correctly"
else:
    print "Sorry, that's not the word I chose. Better luck next time."
    print "The word I chose was: ", correct

raw_input("Press enter to exit.")
