# Python Programme Number 55
# Trivia Challenge: Demostrates use of Files & Exceptions
# Programmer: Mukul Dharwadkar
# Date: 25 June 2006

def open_file(file_name, mode):
    """Open the File"""
    try:
        the_file = open(file_name, mode)
    except(IOError), e:
        print "Unable to open the file", the_file, "Ending Programme.\n", e
        raw_input("\n\nPress enter to exit")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Returns the next block of data from the trivia file."""
    category = next_line(the_file)

    question = next_line(the_file)

    answers =  []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    return category, question, answers, correct, explanation

def welcome(title):
    "Welcome the player and get his/her name."""
    print "\t\tWelcome to the Trivia Challenge!\n"
    print "\t\t", title, "\n"

def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        # while category is not empty as a question
        print category
        print question
        for i in range (4):
            print "\t", i + 1, "-", answers[i]

        # Get the answer
        answer = raw_input("What is your answer?: ")

        # Check the answer
        if answer == correct:
            print "\nRight!!",
            score += 1
        else:
            print "\nWrong",
        print explanation
        print "Score: ", score, "\n\n"

        # Get the next block
        category, question, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()

    print "That was the last question!"
    print "Your final score is: ", score

main()
raw_input("\nPress enter to exit.")
