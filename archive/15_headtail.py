# Python Programme Number 15
# Heads or tails
# Programmer: Mukul Dharwadkar
# Date: 25 February 2006

import random

i = 0
count = 0

# Begin the while loop
while count < 100:
    flip = random.randrange(2)
    if flip == 0:
        #print "Heads"
        i += 1
    else:
    #    print "Tails"
        count += 1
print "You tossed Heads", i, "times and Tails", 100-i, "times."
