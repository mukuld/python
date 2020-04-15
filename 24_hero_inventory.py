# Python Programme Number 24
# Hero's Inventory: Introduction to TUPLES
# Programmer: Mukul Dharwadkar
# Date: 8 March 2006

# Create an empty tuple
inventory = ()

# Treat the tuple as a condition
if not inventory:
    print "You are empty-handed."

raw_input("Press enter to continue.")

# Create a tuple with some items
inventory = ("Sword", "Shield",
             "Armour", "Healing Potion")

# Print the tuple
print "\nThe tuple inventory contains:\n", inventory

# Print each element
print "\nYou have:"
for item in inventory:
    print item

raw_input("Press enter to exit.")
