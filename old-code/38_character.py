# Python Programme Number 38
# Character Creator
# Programmer: Mukul Dharwadkar
# Date: 19 March 2006

points = 30
ATTRIBUTES = {"Wisdom" : 10, "Strength": 7,
              "Health" : 8, "Dexterity" : 8}
choice = 0
response = 0
attrib = []

print \
      """
      Hello and welcome.
      You have 30 points to spend on your attributes.
      Spend wisely as it will define your character.
      You can choose for the following attributes.
      The number in parentheses gives its cost.
      The number on the left gives the choice number
      1. WISDOM(10)
      2. STRENGTH(7)
      3. HEALTH(8)
      4. DEXTERITY(8)
      5. EXIT
      """
response = raw_input("\nWhat would you like to do? Spend points or\
    add points? (s(pend) / a(dd): ")
while points > 0:
    if response == "s":
        choice = int(raw_input("\nWhat would you like to spend on?: "))
        print "You have", points, " points to spend."
        if choice == 5:
            print "Good-bye"
            break
        elif choice == 1 and points > 0:
            points = points - ATTRIBUTES["Wisdom"]
            attrib.append("Wisdom")
            print "You now have", attrib, "and ", points, "points"
        elif choice == 2 and points > 0:
            points = points - ATTRIBUTES["Strength"]
            attrib.append("Strength")
            print "You now have", attrib, "and ", points, "points"
        elif choice == 3 and points > 0:
            points = points - ATTRIBUTES["Health"]
            attrib.append("Health")
            print "You now have", attrib, "and ", points, "points"
        elif choice == 4 and points > 0:
            points = points - ATTRIBUTES["Dexterity"]
            attrib.append("Dexterity")
            print "You now have", attrib, "and ", points, "points"
        else:
            print "\nYou don't have enough points to buy anything."
    elif response == "a":
        print "You have ", attrib
        choice = int(raw_input("\nWhat would you like to give away?: "))
        if choice == 5:
            print "Good-bye"
            break
        elif choice == 1:
            points = points + ATTRIBUTES["Wisdom"]
            del attrib[0]
            print "You now have", attrib, "and ", points, "points"
        elif choice == 2:
            points = points + ATTRIBUTES["Strength"]
            del attrib[1]
            print "You now have", attrib, "and ", points, "points"
        elif choice == 3:
            points = points + ATTRIBUTES["Health"]
            del attrib[2]
            print "You now have", attrib, "and ", points, "points"
        elif choice == 4:
            points = points + ATTRIBUTES["Dexterity"]
            del attrib[3]
            print "You now have", attrib, "and ", points, "points"
            
raw_input("Press enter to exit")
