# Python Programme Number 57
# Trivia Challenge - modified: Demostrates use of Files & Exceptions & stores
# high scores
# Programmer: Mukul Dharwadkar
# Date: 26 June 2006

import cPickle

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

    point_value = next_line(the_file)

    explanation = next_line(the_file)

    return category, question, answers, correct, point_value, explanation

def welcome(title, name):
    """Welcome the player and get his/her name."""
    print "\t\tWelcome to the Trivia Challenge!\n"
    print "\t\t", title, "\n"
    print "Welcome to this episode, ", name

def pickling(name, score):
    """Store the scores and the names in a file & pickle it for future use."""
    score_new = [(name, score)]
    try:
        pickle_file = open("hiscores.dat", "r")
        try:
            score_list = cPickle.load(pickle_file)
            pickle_file.close()
        except(EOFError):
            cPickle.dump(score_new, pickle_file, True)
            score_list = []
    except(IOError):
        pickle_file = open("hiscores.dat", "w+")
        cPickle.dump(score_new, pickle_file, True)
        score_list = []
    score_list.append(score_new[0])
    score_list.sort()
    pickle_file = open("hiscores.dat", "w")
    cPickle.dump(score_list, pickle_file, True)
    return score_list

def main():
    name = raw_input("What is your name? ")
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title, name)
    score = 0


    # get first block
    category, question, answers, correct, point_value, explanation = next_block(trivia_file)
    while category and point_value:
        # while category is not empty ask a question
        print category
        print question
        for i in range(4):
            print "\t", i + 1, "-", answers[i]

        # Get the answer
        answer = raw_input("What is your answer?: ")

        # Check the answer
        if answer == correct:
            print "\nRight!!",
            score += int(point_value)
        else:
            print "\nWrong",
        print explanation
        print "Score: ", score, "\n\n"

        # Get the next block
        category, question, answers, correct, point_value, explanation = next_block(trivia_file)

    trivia_file.close()

    print "That was the last question!"
    print "Your final score is: ", score
    score_list = pickling(name, score)
    print score_list

main()
raw_input("\nPress enter to exit.")
