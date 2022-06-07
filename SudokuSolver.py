import numpy as np
import Generator

grid = Generator.randomize()

def possible(y,x,n):
	global grid
	for i in range(0,9):
		if grid[y][i] == n:
			return False
	for i in range(0,9):
		if grid[i][x] == n:
			return False
	x0 = (x//3)*3
	y0 = (y//3)*3
	for i in range(0,3):
		for j in range(0,3):
			if grid[y0+1][x0+1] == n:
				return False
	return True


def solve():
	global grid
	for y in range (9):
		for x in range (9):
			if grid[y][x] == 0:
				for n in range (1,10):
					if possible(y,x,n):
						grid[y][x] = n
						solve()
						grid[y][x] = 0
				return
	print (np.matrix(grid))
	input("more?")

solve()

print("Done")