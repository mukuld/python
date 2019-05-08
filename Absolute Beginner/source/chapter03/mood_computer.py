# Mood Computer
# Demonstrates the if-elif-else structure
# Michael Dawson - 12/29/02

import random

print "I sense your energy.  Your true emotions are coming across my screen."
print "You are..."

mood = random.randrange(3)

if mood == 0:
    # happy
    print \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | .     . |
       |  `...`  |
       -----------
                   """
elif mood == 1:
    # neutral  
    print \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | ------  |
       |         |
       -----------
                   """
elif mood == 2:
    # sad
    print \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       |  .'.    |
       | '   '   |
       -----------
                   """
else:
    print "Illegal mood value!  (You must be in a really bad mood)."

print "...today."

raw_input("\n\nPress the enter key to exit.")






