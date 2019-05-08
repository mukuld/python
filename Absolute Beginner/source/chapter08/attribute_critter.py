# Attribute Critter
# Demonstrates creating and accessing object attributes
# Michael Dawson - 3/23/03

class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        print "A new critter has been born!"
        self.name = name

    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep

    def __cmp__(self, other):
        if self.name > other.name:
            return 1
        if self.name < other.name:
            return -1
        if self.name == other.name:
            return 0      

    def talk(self):
        print "Hi.  I'm", self.name, "\n"

# main
crit1 = Critter("Poochie")
crit1.talk()

crit2 = Critter("Randolph")
crit2.talk()

print "Printing crit1:"
print crit1

print "Directly accessing crit1.name:"
print crit1.name

raw_input("\n\nPress the enter key to exit.")
