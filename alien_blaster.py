'''
Created on Jan 11, 2010

@author: Mukul Dharwadkar
'''
# Demonstrates object interaction

class Player(object):
    """A player in the shooter game"""
    def blast(self, enemy):
        print "The player blasts the enemy.\n"
        enemy.die()
        
class Alien(object):
    "The villian in the shooter game"""
    def die(self):
        print "And the alien says, 'Oh no. So finally you got me....'"

#main
print "\t\tDeath of an alien\n"

hero = Player()
invader = Alien()
hero.blast(invader)

raw_input("Press Enter to Exit")    