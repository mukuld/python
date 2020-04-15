# Python Programme Number 31
# Hero's inventory v3.0: Demonstrates use of lists and list methods
# Programmer: Mukul Dharwadkar
# Date: 16 March 2006

# Create a list to depict the items the Hero has and display it

inventory = ["sword", "armour", "shield", "healing potion"]
print "Your have"
for item in inventory:
    print item

raw_input("\nPress enter to continue.")

# Get the length of the list

print "You have", len(inventory), "items in your possession."
raw_input("\nPress enter to continue.")

# Test membership with the in function
if "healing potion" in inventory:
    print "Use your healing potion to heal any wounds."
    print "You will live to fight another day."

# Use indexing to display one item
index = int(raw_input("\nEnter the index number for an item in inventory: "))
print "At index", index, "you have", inventory[index]

# Display multiple items using slicing techniques.
begin = int(raw_input("\nEnter the starting index number: "))
end = int(raw_input("\nEnter the ending index number: "))
print "Inventory[", begin, ":", end, "]\t\t",
print inventory[begin:end]

raw_input("\nPress enter to continue.")

# Concatenate two lists
chest = ["gold", "gems"]
print "Lucky you, you have found a chest full of."
print chest
print "You add the contents of chest to your inventory."
inventory += chest
print "You now have:"
print inventory

raw_input("\nPress enter to continue.")

# Assign by index

print "You trade your sword with a cross-bow."
inventory[0] = "cross-bow"
print "Now you have:"
print inventory

raw_input("\nPress enter to continue.")

# Assign by slice

print "You buy orb of future telling with your gold and gems."
inventory[4:6] = ["orb of future telling"]
print "Now you have:"
print inventory

raw_input("\nPress enter to continue.")

print "You meet a formidable foe. In the great battle that ensues",
print "Your shield is damaged totally."
del inventory[2]
print "Now you have:"
print inventory

raw_input("\nPress enter to continue.")

# delete a slice

print "Tired by such a long and ardous journey, you lie down to rest."
print "While you are sleeping, thieves steal your cross-bow and armour."
del inventory[:2]
print "Now you have:"
print inventory

raw_input("\nPress enter to continue.")
