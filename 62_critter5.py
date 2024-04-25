# Python Programme Number 62
# Private critter: Demonstrates private variables and methods
# Programmer: Mukul Dharwadkar
# Date: 3 July 2006

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, mood):
        print "A new critter has been born!"
        self.name = name        # Public Attribute
        self.__mood = mood      # Private Attribute

    def talk(self):
        print "\nI'm", self.name
        print "Right now I feel", self.__mood, "\n"

    def __private_method(self):
        print "This is a private method."

    def public_method(self):
        print "This is a public method"
        self.__private_method()

# main
crit = Critter(name = "Poochie", mood = "Happy")
crit.talk()
crit.public_method()

raw_input("\n\nPress enter to exit")
