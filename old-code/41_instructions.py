# Python Programme Number 41
# Display instructions
# Demonstrates the use of functions
# Programmer: Mukul Dharwadkar
# Date: 26 March 2006

def instructions():
    """Display the game instructions."""
    print \
    """
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe
    This is going to be the ultimate showdown between you human brain and
    my infinitely superior silicon processor.

    You will make you move know by entering a number between 0 - 8 (both included).
    The number will correspond to the board position as shown below:

            0  |  1  |  2
           ----|-----|----
            3  |  4  |  5
           ----|-----|----
            6  |  7  |  8

    Prepare yourself human!!! The battle is about to begin.\n
    """

# main body of the programme.
print "Here are the instructions for the Tic-Tac-Toe."
instructions()

print "Here they are again. Just in case if you missed earlier."
instructions()

print "Even you should understand the game by now..."

raw_input("Press enter to exit.")
