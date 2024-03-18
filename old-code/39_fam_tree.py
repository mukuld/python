# Python Programme Number 39
# Father and Son family tree
# Programmer: Mukul Dharwadkar
# Date: 20 March 2006

# Create the dictionary containing father and son pairs
fam_tree = {"Jayant" : "Mukul", "Mukul" : "Aroon", "Abhir" : "Anand",
            "Anand" : "Aroon", "Aroon" : "Mukund", "Srujan" : "Ambarish",
            "Ambarish" : "Brahmanand", "Mukund" : "Vyankatesh"}

print """
    Welcome to the family tree program.
    Here you can find out who is father of who.
    Choose from the following menu options below

    0 = EXIT
    1 = FIND OUT FATHER OF SOMEONE
    2 = LIST NAMES OF SONS
    3 = LIST NAMES OF FATHERS
    4 = ADD A FATHER SON PAIR
    5 = MODIFY A FATHER SON PAIR
    6 = DELETE A FATHER SON PAIR
    7 = LIST FATHER SON PAIRS
    """

CHOICELIST = ("1", "2", "3", "4", "5", "6", "7")
#def choice():
choice = "1"
while choice != "0":
    choice = raw_input("What would you like to do?: ")
    if choice == "0":
        print "Goodbye"
    elif choice == "1":
        son = raw_input("Enter the name of son who you want to check: ")
        father = fam_tree[son]
        print father, "is the father of ", son
    elif choice == "2":
        sons = fam_tree.keys()
        print "The sons in the dictionary are: ", sons
    elif choice == "3":
        fathers = fam_tree.values()
        print "The fathers in the dictionary are: ", fathers
    elif choice == "4":
        son = raw_input("Enter the name of son you want to add: ")
        if son not in fam_tree:
            father = raw_input("Enter the name of father you want to add: ")
            fam_tree[son] = father
            print "The new pair of father and son has been added for ", son
            print "\nThe list is now ", fam_tree, "."
        else:
            print "That name already exists in the list. Try modifying it (option 5)"
    elif choice == "5":
        son = raw_input("Enter the name of the son whose father you want to modify: ")
        if son in fam_tree:
            father = raw_input("What is the correct name of his father: ")
            fam_tree[son] = father
            print "The record for ", son, "has been updated."
        else:
            print "\nThe name of the son doesn't exist. Try adding it (option 4)."
    elif choice == "6":
        son = raw_input("Enter the name for whom you want to delete the record: ")
        if son in fam_tree:
            del fam_tree[son]
        else:
            print "Error!!!. You cannot delete what does not exist. \nThe record does not exist here."
    elif choice == "7":
        print "So, you want the entire list. Hmmm...."
        print "Here you go!!!"
        #print fam_tree
        print "=============================="
        print "|\t SON\t| FATHER\t|"
        print "=============================="
        for son in fam_tree:
            print "|",son,"\t|", fam_tree[son],"\t|"
            print "=============================="
    else:
        print "Invalid input!! That entry is not allowed. Try from options above."

raw_input("Press enter to exit")
