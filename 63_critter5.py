# Python Programme Number 63
# Property critter: Demonstrates get and set methods and properties
# Programmer: Mukul Dharwadkar
# Date: 3 July 2006

class Critter(object):
    """ A virtual pet"""
    def __init__(self, name):
        print "A new critter has been born."
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if new_name == "":
            print "A critter's name cannot be empty"
        else:
            self.__name = new_name
            print "Name change successful"

    name = property(get_name, set_name)

    def talk(self):
        print "\nHi, I'm", self.name

# main
crit = Critter("Poochie")
crit.talk()

print "\nMy critter's name is",
print crit.name
print "\nAttempting to change my critter's name"
crit.name = ""
print "\nAttempting to change my critter's name again."
crit.name = "Randolph"

crit.talk()

raw_input("\n\nPress enter to exit")
