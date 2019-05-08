# Simple Critter
# Demonstrates a basic class and object 
# Michael Dawson - 3/23/03

class Critter(object):
    """A virtual pet"""
    def talk(self):
        print "Hi.  I'm an instance of class Critter."

# main
crit = Critter()
crit.talk()

raw_input("\n\nPress the enter key to exit.")
