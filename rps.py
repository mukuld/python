# An all-time favorite game of Rock Paper Scissors.
# Programmer: Mukul Dharwadkar
# Date: June 27 2017

import random

def instructions():
	"""Displays the game instructions"""
	
	print('''\n
	Today we will play the perennial favorite game of...\n
	Rock! Paper!! Scissors!!!.\n
	The objective of the game is to outthink your opponent (in this case me) and defeat.\n
	The rules are very simple\n
	1. Paper covers the Rock\n
	2. Rock breaks the Scissors\n
	3. Scissors cut the Paper\n\n
	
	Choose your move from the following:\n
	1. Paper (p)\n
	2. Rock (r)\n
	3. Scissors (s)\n\n
	
	Are you ready? Alright then, let\'s play...\n''')

def get_name():
	"""Get player's name"""
	
	print(
	"""First of all, let's get to know each other a little better.
	My name is Compy...
	What's yours?
	""")
	player_name = input("What is your name: ")
	#print player_name
	return player_name
	
def greet_player(name):
	"""Let's be polite and greet each other properly"""
	
	print("How are are you doing, ", name)

def legal_moves():
	"""Define the legal moves"""
	legal_moves = ("r", "p", "s")
	return legal_moves
	
def player_move():
	"""Players choose their move"""
	move = None
	while move not in moves:
		move = input("What is your move %s? --> " % name)
	return move
	
def computer_move():
	"""The computer will choose its move in this function"""
	move = random.choice(moves)
	print("Computer's move is",  move)
	return move

def compare_moves(p_move, c_move):
	"""We will now compare the moves the human and computer make and then take the output
	to declare the winner"""
#	tie = "It's a tie"
	if p_move == "r" and c_move == "p":
		return "computer"
	elif p_move == "r" and c_move == "s":
		return "human"
	elif p_move == "p" and c_move == "s":
		return "computer"
	elif p_move == "p" and c_move == "r":
		return "human"
	elif p_move == "s" and c_move == "r":
		return "computer"
	elif p_move == "s" and c_move == "p":
		return "human"
			
def declare_winner(winner):
	if winner == "human":
		print(name, "wins. Congratulations and well played!!!")
	elif winner == "computer":
		print("Computer wins. Better luck next time", name, ".")
	else:
		print("It's a tie")


#main body of the program
instructions()
name = get_name()
moves = legal_moves()
greet_player(name)
p_move = player_move()
c_move = computer_move()
winner = compare_moves(p_move, c_move)
declare_winner(winner)
