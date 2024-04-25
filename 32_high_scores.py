# Python Programme Number 32
# High Scores Keeper: Demonstrates lists methods
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
          1 = Show Scores
          2 = Add a score
          3 = Delete a score
          4 = Sort Scores
          """

    choice = raw_input("Please make a choice: ")
    print

    # Exit the program if user enters 0
    if choice == "0":
        print "Good-bye."

    # List the high scores table
    elif choice == "1":
        print "High Scores"
        for score in scores:
            print score

    # Add a new high score
    elif choice == "2":
        score = int(raw_input("What score did you get?: "))
        scores.append(score)

    # Remove a high score
    elif choice == "3":
        score = int(raw_input("Delete which score?: "))
        if score in scores:
            scores.remove(score)
        else:
            print score, "isnt in the high scores list."

    # Sort the scores for better readability
    elif choice == "4":
        scores.sort()
        # Reverse the list so that the highest score is at the top
        scores.reverse()

    # It is likely that user will enter something other than expected choices
    # even when instructions are right there on the screen.
    else:
        print "Sorry, but", choice, "Isn't a valid choice"
        print "Please choose form the list fron above."

raw_input("\n\nPress enter to exit.")
