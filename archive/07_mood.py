# Python Programme Number 7
# Display mood of the user
# Programmer: Mukul Dharwadkar
# Date: 22 February 2006

import random

print "You are normally very energetic so that you exude you mood."
print "\nToday you are..."

mood = random.randrange(3)

if mood == 0:
#Happy!!!
    print """
        ^^^^^
       | o o |
      (   |   )
       |.   .|
       | ... |
       ------
		"""

elif mood == 1:
# Neutral
    print """
        ^^^^^
       | o o |
      (   |   )
       |     |
       | ... |
       ------
		"""

elif mood == 2:
# Sad
    print """
        ^^^^^
       | o o |
      (   |   )
       | ... |
       |.   .|
       ------
		"""

else:

    print "You seem to be in a very bad mood"

#raw_input("\n\nPress enter to exit")



