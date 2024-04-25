# Python Programme Number 14
# Fortune Teller
# Programmer: Mukul Dharwadkar
# Date: 25 February 2006
#
# This programme will choose from a set of five pre-defined fortunes
# and print any of them randomly everytime the programme is run.

import random

fort1 = "You are very lucky today."
fort2 = "You will meet true love today."
fort3 = "Beware of strangers."
fort4 = "You should not lose heart in face of difficulties."
fort5 = "You might meet a long forgotten friend today."

num = random.randrange(5)

if num == 0:
    print fort1
elif num == 1:
    print fort2
elif num == 2:
    print fort3
elif num == 3:
    print fort4
else:
    print fort5

#raw_input("Press enter to exit.")
