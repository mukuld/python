# Program to sort a text file alphabetically
# Progammer: Mukul Dharwadkar
# Date: 29 April 2020
# Python Version 3
# Program version 1: Basic program with sort and hardcoded output file name
# Program version 2: Basic program name with sort and output file name as an argument

import sys

def sort_file():
    with open(sys.argv[1], "r") as file1:
        newFile = sys.argv[2]
        nf = open(newFile, "w+")
        for line in sorted(file1):
            nf.write(line)
        nf.close()

sort_file()