# Program to find the LCM with remainders as
# [8, 7, 6, 5, 4, 3, 2, 1] when a number is divided by
# [9, 8, 7, 6, 5, 4, 3, 2] respectively
# Programmer: Mukul Dharwadkar
# Date: 2 May 2020
# Python version 3

Y = 3
remain_list = [8, 7, 6, 5, 4, 3, 2, 1]
div_list = [9, 8, 7, 6, 5, 4, 3, 2]

while True or Y % 2 != 0:
    ans_list = []
    for div in div_list:
        remainder = Y % div
        ans_list.append(remainder)
    if ans_list == remain_list:
        print(Y)
        break
    Y += 1