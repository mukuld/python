# Python Programme Number 60
# Attribute Critter: Demonstrates creating and accessing object attributes
# Programmer: Mukul Dharwadkar
# Date: 3 July 2006

class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        print "A new critter has been born"
        self.name = name
    def __str__(self):
        rep = "Critter Object\n"
        rep += "name: " + self.name + "\n"
        return rep

    def talk(self):
        print "Hi, I'm", self.name, "\n"

# main
crit1 = Critter("Poochie")
crit1.talk()

crit2 = Critter("Randolph")
crit2.talk()

print "Printing crit1:"
print crit1

print "Directly accessing crit1.name"
print crit1.name

raw_input("\nPress enter to exit")
