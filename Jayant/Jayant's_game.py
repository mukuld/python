#Guess My Number
#
#The computer picks a random number from 1-100
#The player tries to guess it and the computer lets
#the player know if the guess is too high, too low 
#or right on the money 
import random
print
print
print
print
print "\tWelcome to 'Guess My Number'!"
print "\tI'm thinking of a number between 1 and 100."
print "\tTry to guess it in as few attempts as you can.\n"
# set the initial values
the_number = random.randrange(100) + 1
guess = int(raw_input("\tTake a guess: "))
tries = 1
# guessing loop
while (guess != the_number):
	if (guess > the_number):
		print "\tLower......"
	else:
		print "\tHigher....."
	guess = int(raw_input("\tTake a guess: "))
	tries+=1
print "\tYou guessed it! The number was", the_number
print "\tCongratulations human you succeded in the dumbest game in the world, it only took you", tries, "tries!\n"
#raw_input("\n\nPress the enter key to exit.")