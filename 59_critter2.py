# Python Programme Number 59
# Constructor Critter: Demonstrates constructor
# Programmer: Mukul Dharwadkar
# Date: 3 July 2006

class Critter(object):
    """A virtual pet"""
    def __init__(self):
        print "A new critter has been born"

    def talk(self):
        print "\nHi. I'm an instance of class critter."

# main
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

raw_input("\nPress enter to exit")
