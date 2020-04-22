# Program to determine square root of any given number
# Programmer: Mukul Dharwadkar
# Date: Apr 15 2020
# Python version 3

def get_number():
    response = None
    while response is None:
        response = float(input("Please choose a number to find a square root of: "))
    return response

def create_guess(inp):
    guess = inp / 2
    return guess

def check_square(num, orig_num):
    square = num * num
    while square - orig_num > 0.00000001 or square - orig_num < 0:
        num = find_new_guess(num, orig_num)
        square = num * num
    print(f"The square root of {orig_num} is {num:.2f}")

def find_new_guess(old_guess, orig_num):
    new_guess = (old_guess + (number / old_guess))/2
    return new_guess


number = get_number()
check_square(create_guess(number), number)