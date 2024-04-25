# Python Programme Number 58
# Simple Critter: Demonstrates class & object
# Programmer: Mukul Dharwadkar
# Date: 03 July 2006

class Critter(object):
    """A virtual pet"""
    def talk(self):
        print "Hi. I'm an instance of class Critter"

# main
crit = Critter()
crit.talk()

raw_input("\n\nPress enter to exit")
