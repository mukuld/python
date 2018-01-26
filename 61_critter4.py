# Python Programme Number 61
# Classy Critter: Demonstrates class attributes and static methods.
# Programmer: Mukul Dharwadkar
# 3 July 2006

class Critter(object):
    """A virtual pet"""
    total = 0

    def status():
        print "\n the total number of critters is", Critter.total

    status = staticmethod(status)

    def __init__(self, name):
        print "A critter has been born"
        self.name = name
        Critter.total += 1

# main
print "Accessing the class attribute Critter.total:",
print Critter.total

print "\nCreating Critters."
crit1 = Critter("critter 1")
crit2 = Critter("critter 2")
crit3 = Critter("critter 3")

Critter.status()

print "\nAccessing the class attribute through an object:",
print crit1.total

raw_input("\nPress enter to exit.")
