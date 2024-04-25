# Program to find LCM of given two numbers
# Date: May 6 2020
# Programmer: Mukul Dharwadkar
# Python Version 3

def my_lcm():
    num1 = int(input("Please enter first number: "))
    num2 = int(input("Please enter second number: "))
    o_num1 = num1
    o_num2 = num2
    if num1 > num2:
        temp = num2
        num2 = num1
        num1 = temp
    num1_test = num1
    num2_test = num2
    num1_list = []
    num2_list = []
    i = 1
    while True:
        num1_test = num1 * i
        num1_list.append(num1_test)
        num2_test = num2 * i
        num2_list.append(num2_test)
        for j in range(len(num1_list)):
            for k in range(len(num2_list)):
                if num1_list[j] == num2_list[k]:
                    print(f"The LCM of {o_num1} and {o_num2} is {num1_test}")
                    return
                k += 1
            j += 1
        i += 1

my_lcm()