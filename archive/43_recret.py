# Python Programme Number 43
# Recieve and return: Demonstrates functions
# Programmer: Mukul Dharwadkar
# Date: 27 March 2006

def display(message):
    print message

def give_me_five():
    five = 5
    return five

def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = raw_input(question).lower()
    return response

# main
display("My name is Mukul Dharwadkar")

number = give_me_five()
print "Here's what I got from give_me_five():", number

answer = ask_yes_no("\nPlease enter 'y' or 'n': ")

print "Thanks for entering:", answer


raw_input("Press enter to exit.")
