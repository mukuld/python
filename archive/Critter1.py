'''
Created on Dec 23, 2009

@author: mdharwadkar
'''
#Simple Critter
#Demonstration of a basic class and object

class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        print "A new pet has been born..."
        self.name = name
        
    def __str__(self):
        rep = "Critter object\n"
        rep += "name: "+ self.name + "\n"
        return rep
    
    def talk(self):
        print "Hi. I'm", self.name, "\n"
        
    def jump(self):
        print "Look how high I can jump \n\n"
        
    def calc(self, x, y):
        answer = x + y
        print "You gave me", x, "and", y
        print "The sum of", x, "and", y, "is:", answer
                
#main
pet1 = Critter("Shital")
pet1.talk()
pet1.jump()

pet2 = Critter("Nandini")
pet2.talk()
pet2.calc(5234, 2234)

print pet1
print pet2
raw_input("\n\nPress Enter to exit")