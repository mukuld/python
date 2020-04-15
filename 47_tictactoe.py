# Python Programme Number 47
# Tic Tac Toe game
# Demostrates use of functions
# Programmer: Mukul Dharwadkar
# Date: 31 March 2006

# Define global constants to be used throughout this programme
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

# This function displays the instructions of the game.
def display_instruct():
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
# This function asks a yes or no question and returns the response
def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = raw_input(question).lower()
    return response

# This function asks the player to enter a number within the range.
# It returns the number specified within the range.

def ask_number(question, low, high):
    """Ask for a number within the range"""
    response = None
    while response not in range(low, high):
        response = int(raw_input(question))
    return response

# The next function asks the player whether s/he wants to go first
# This function also returns the computer's piece to human piece.
def pieces():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Do you require the first move?(y/n): ")
    if go_first == "y":
        print "\nThen take the first move. You will need it."
        human = X
        computer = O
    else:
        print "Your bravery will be your undoing... I will go first."
        computer = X
        human = O
    return computer, human

# This function creates a new board
# Essentially it creates a new list with nine elements,
# sets it to EMPTY and returns it.
def new_board():
    """Create a new game board."""
    board = []
    for sqaure in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

# This function displays the board passed to it by preceding new_board function
# The possible elements for each position on the board are:
# A space, a X or a O.
def display_board(board):
    "Display Game board on screen."""
    print "\n\t", board[0], "|", board[1], "\t|", board[2]
    print "\t", "------------"
    print "\t", board[3], "|", board[4], "\t|", board[5]
    print "\t", "------------"
    print "\t", board[6], "|", board[7], "\t|", board[8], "\n"

# This function creates and defines a list of legal moves for the game.
def legal_moves(board):
    """Create a list of legal moves."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

# This function receives a board and returns the winner.
# To identify a winner, first define the ways to win.
# This is done by defining a constant WAYS_TO_WIN & create a tuple which
# contains all the 8 ways to get three same characters in a row.
# There are four possibilities for a winner. Either a X or an O, a tie or None.
def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

# The next function receives a board and the human move
# It returns the square number where the player wants to move.
def human_move(board, human):
    """Get human move"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8): ", 0, NUM_SQUARES)
        if move not in legal:
            print "\nThat square is already occupied, foolish human. Choose another.\n"
    print "Fine..."
    return move

# This function receives the board, the computer's piece and human's piece.
# It returns the computer's move.   
def computer_move(board, computer, human):
    """Make computer move."""
    # Make a copy to work with since function will be changing list.
    board = board[:]
    # The best positions to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print "I shall take square number",
    # If computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print move
            return move
        # If this move doesn't work, undo it.
        board[move] = EMPTY
        # If human can win using any move, block that move
        for move in legal_moves(board):
            board[move] = human
            if winner(board) == human:
                print move
                return move
        # If this move does not allow human to win, undo it.
        board[move] = EMPTY
        # Since no one can win, pick the next best move.
        for move in BEST_MOVES:
            if move in legal_moves(board):
                print move
                return move

# This function defines the next turn
def next_turn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X

# This function receives the winner and then congratulates the winner or
# declares a tie.
def congrat_winner(the_winner, computer, human):
    """Congratulate the winner"""
    if the_winner != TIE:
        print the_winner, "won\n"
    else:
        print "It's a tie.\n"
    if the_winner == computer:
        print "As I predicted, human, I am invincible and truimphant once more\n" \
              "Computers are superior to human race...."

    elif the_winner == human:
        print "No! No!! No!!! It can't be true. You have cheated me...\n" \
              "But I will beat you the next time!!!"

    elif the_winner == TIE:
        print "You escaped this time with luck, human. \n" \
              "Next time you won't be so lucky!!!"

# The main function of the program
def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

# Start the program by calling the main() function
main()
raw_input("\n\nPress enter to exit.")

