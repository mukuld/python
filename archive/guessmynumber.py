import random

#Generating a random number from 1 - 100

number = random.randrange(100) + 1
#print(number)

#Welcome to....GUESS MY NUMBER!

print("Greetings. My name is Invincible, Vince for short")
ask_name = input("What is your name?:")
print("Hello %s" % ask_name)
print("You really think you can beat me? Never!")

#Define a variable to hold the user's guess. This variable will be used throughout the program, mostly in loops
guess = int(input("Guess a number from 1 to 100:"))

#Define a variable that will hold the number of tries it takes for the user to guess the number
#Set tries to 1
tries = 1

#Start the process of trial and error
while guess != number:
  if guess < number:
    print("Your guess is too low")
  else:
    print("Your guess is too high")
  print("Nope! Try again!")
  tries += 1
  guess = int(input("Guess a number from 1 to 100:"))
  
print("Okay, {}, fine, you beat me".format(ask_name))
print("Yes, the number was {}" .format(number))
print("It took you {} tries to guess the number" .format(tries))