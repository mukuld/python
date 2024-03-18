# Program to find the value of PI based on Madhava-Leibniz formula
# Reference URL: https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
# Programmer: Mukul Dharwadkar
# Date: April 29 2020
# Python Version 3
# Program version 1

def get_number():
    response = None
    while response is None:
        response = float(input("Please choose a number to get the accuracy of PI upto: "))
    return response

def calulate(num):
    counter = 1
    add_start = 5
    sub_start = 3

    sub_placeholder = 1
    add_placeholder = 0
    pi_place = 0

    while counter <= num:
    #    sub_placeholder = sub_placeholder - (1 / sub_start)
    #    add_placeholder = add_placeholder + (1/add_start)
    #    sub_start += 4
    #    add_start += 4
        pi_place = pi_place + ((-1)**(counter - 1)/((2 * counter) - 1))
    #    pi_place_holder = sub_placeholder + add_placeholder
        counter += 1
    pi_value = 4 * pi_place
    print(f"The value of pi is {pi_value}")

number = get_number()
calulate(number)
