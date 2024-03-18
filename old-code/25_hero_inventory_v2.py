# Python Programme Number 25
# Hero's Inventory v2.0: Demonstrates the power TUPLES
# Programmer: Mukul Dharwadkar
# Date: 8 March 2006

# Create an tuple with some items and display
inventory = ("Sword", "Shield",
             "Armour", "Healing Potion")

print "\nYou have:"
for item in inventory:
    print item

raw_input("Press enter to continue.")

# Get the length of the tuple
print "\nYou have", len(inventory), "items in your possession."

raw_input("Press enter to continue.")

# Test for membership with in
if "Healing Potion" in inventory:
    print "\n\nBachenge to aur bhi ladenge."

# Display one item through indexing
index = int(raw_input("\nEnter the index number for an item in the inventory: "))
print "At index", index, "is", inventory[index]

# Display a slice
begin = int(raw_input("\nEnter the index number to begin a slice: "))
end = int(raw_input("\nEnter the index number to end the slice: "))
print "inventory[", begin, ":", end, "]\t\t"
print inventory[begin:end]

raw_input("Press enter to continue.")

# Concatenate two tuples
chest = ("gold", "gems")
print "You find a treasure chest. It contains:"
print chest
print "You add the contents of the chest to your inventory."
inventory += chest
print "Your inventory is now:"
print inventory

raw_input("Press enter to continue.")
