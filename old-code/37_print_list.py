# Python Programme Number 37
# Print list of words randomly without repeating
# Programmer: Mukul Dharwadkar
# Date 19 March 2006

import random

# Create a constant list to print
WORDS = ("OVERUSED", "SHITAL", "MUKUL", "JAYANT", "INDIA", "CLAM", "GUAM",
         "PUCK", "COFFEE", "HOUSE", "LAPTOP", "COMPUTER", "HACKER", "sheetal",
         "delllaptop", "jurassic", "sholay", "keyboard", "synthesizer",
         "flatpanel", "refrigerator", "workhorse", "difficult", "python",
         "linux", "redhat", "windows", "microsoft", "dharwadkar", "infosys",
         "philips", "yamaha", "xylophone", "NANDINI")

num = len(WORDS)
printed = []        # An empty list to hold already listed words

while len(printed) != len(WORDS):
    word = random.choice(WORDS)
    if word not in printed:
        print word
        printed.append(word)
raw_input("Press enter to exit.")
