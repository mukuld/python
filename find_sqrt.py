#Program to determine square root of any given number
# Programmer: Mukul Dharwadkar
# Date: Apr 15 2020

def get_number():
    response = None
    while response is None:
        response = int(input("Please choose a number to find a square root of: "))
    #print(response)
    return response

def create_guess(inp):
    guess = inp / 2
    print(guess)
    return guess

def check_square(num, orig_num):
    square = num * num
    if square == orig_num:
        print(f"Square Root of {orig_num} is {num}")
    else:
        print("Try again")

## Start here. Work to find a new guess by implementing the logic
## new_guess = (old_guess + (number / old_guess))/2
## And check the square again of the new_guess
## Adding a comment
def find_new_guess():


number = get_number()
#create_guess(get_number())
check_square(create_guess(number), number)