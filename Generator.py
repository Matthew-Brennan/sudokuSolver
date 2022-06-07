import Solver
import random 

def initialize():
	board = [
	    [0,0,0,0,0,0,0,0,0],
	    [0,0,0,0,0,0,0,0,0],
	    [0,0,0,0,0,0,0,0,0],
	    [0,0,0,0,0,0,0,0,0],
	    [0,0,0,0,0,0,0,0,0],
	    [0,0,0,0,0,0,0,0,0],
	    [0,0,0,0,0,0,0,0,0],
	    [0,0,0,0,0,0,0,0,0],
	    [0,0,0,0,0,0,0,0,0]]

	return board

def randomize():
	board = initialize()
	count = 0
	array = [1,2,3,4,5,6,7,8,9]

	#Fill in the top left box(3x3) randomly. This acts as a seed to randomly generate the rest of the grid
	for i in range(0,3):
		for j in range(0,3):
			board[i][j] = array.pop(random.randrange(0,len(array)))
	#fill in the rest of the board
	Solver.solve(board)
	

	#remove 60 numbers from the board to create the puzzle
	while count < 60:
		pos = (random.randrange(0,9),random.randrange(0,9))
		if board [pos[0]] [pos[1]] != 0:
			board [pos[0]] [pos[1]] = 0
			count = count + 1	
			
	return board







