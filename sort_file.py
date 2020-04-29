# Program to sort a text file alphabetically
# Progammer: Mukul Dharwadkar
# Date: 29 April 2020
# Python Version 3
# Program version 1

import sys

def sort_file():
    with open(sys.argv[1], "r") as file1:
        newFile = "sortedsongs.txt"
        nf = open(newFile, "w+")
        for line in sorted(file1):
            nf.write(line)

sort_file()