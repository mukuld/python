# Hero's Inventory
# Demonstrates tuple creation
# Michael Dawson - 1/29/03

# create an empty tuple
inventory = ()

# treat the tuple as a condition
if not inventory:
    print "You are empty-handed."

raw_input("\nPress the enter key to continue.")

# create a tuple with some items
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

# print the tuple
print "\nThe tuple inventory is:\n", inventory

# print each element in the tuple
print "\nYour items:"
for item in inventory:
    print item

raw_input("\n\nPress the enter key to exit.")
