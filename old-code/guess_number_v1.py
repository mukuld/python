#Program to guess a number that computer has chosen for the user.
#Programmer: Mukul Dharwadkar
#Date: 5th November 2019

import random
LIMIT = 3

""" The idea here is to write top down software and use functions as much as possible
in order to make the code reusable. The goal is to extract some of the functions out
of this program and make into independent modules that could be called by other programs
as needed.
"""

def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_name():
    print("Welcome to the greatest guessing game. If you can guess this, you should start betting on the stock market or head to Las Vegas")
    user_name = input("What is your name? ")
    return user_name

def choose_random_number():
    number = random.randrange(100) + 1
    return number

def guess_number(name, number):
    tries = 1
    print("Hello", name, "!")
    ask_yes_no("Are you ready to play?")
    print("OK, I have chosen a number.")
    choice = int(input("What is your choice?"))
    while (choice != number) and (tries <= (LIMIT - 1)):
        if (choice < number):
            print("Your guess is too low. Go higher")
        else:
            print("Your guess is too high. Go lower")
        choice = int(input("What is your choice?"))
        tries += 1

    if (tries > (LIMIT - 1)):
        print("You lose. Game Over. The number was", number)
    else:
        print("You guessed the number. It was ", number)
        print("You guess in ", tries, " tries.")
    
#    response = (ask_yes_no("Do you want to play again?")).lower()
#    while response is "y":
#        guess_number(number, num)

name = ask_name()
num = choose_random_number()
guess_number(name, num)