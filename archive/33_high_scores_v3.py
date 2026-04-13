# Python Programme Number 33
# High Scores Keeper v2.0: Demonstrates lists methods and advanced techniques
# Programmer: Mukul Dharwadkar
# Date: 18 March 2006

# This programme allows the user of the programme to maintain high scores
# The user can add, delete or modify high scores.

scores = []
choice = None

# While the menu choice is not 0 (None), the program will continue to run.

while choice != "0":

    print \
          """
          High Scores Keeper
          0 = Exit
          1 = List Scores
          2 = Add a score
          """

    choice = raw_input("Please make a choice: ")
    print

    # Exit the program if user enters 0
    if choice == "0":
        print "Good-bye."

    # List the high scores table
    elif choice == "1":
        print "====================="
        print "NAME\t | \tSCORE"
        print "====================="
        for entry in scores:
            score, name = entry    
            print name, "\t | \t", score
            print "====================="

    # Add a new high score
    elif choice == "2":
        name = raw_input("Enter the player's name: ")
        score = int(raw_input("What score did the player get?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]

    # even when instructions are right there on the screen.
    else:
        print "Sorry, but", choice, "Isn't a valid choice"
        print "Please choose form the list fron above."

raw_input("\n\nPress enter to exit.")
