# Python Programme Number 9
# The Hero always loses the battle in this programme
# Programmer: Mukul Dharwadkar
# Date: 22 February 2006

print "The Hero fights a lone battle against the trolls army."
print "There is no end in sight for the trolls coming"
print "They smell horrible and look terrible"
print "The Hero takes out is swords and prepares to battle"

health = 100
damage = 3
trolls = 0

while health > 0:
    trolls += 1
    health = health - damage

    print "The hero fights valiantly and defeats a troll," \
        " but sustains", damage, "damage points.\n"

print "The hero fought valiantly and defeated", trolls, "trolls"
print "But alas, there were just too many trolls"
print "\n\n\n\t\tGoodbye!!!"
