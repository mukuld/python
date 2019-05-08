# Constructor Critter
# Demonstrates constructors
# Michael Dawson - 3/23/03

class Critter(object):
    """A virtual pet""" 
    def __init__(self):
        print "A new critter has been born!"

    def talk(self):
        print "\nHi.  I'm an instance of class Critter."

# main
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

raw_input("\n\nPress the enter key to exit.")
