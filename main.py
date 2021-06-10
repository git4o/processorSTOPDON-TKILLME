#tic tac toe
import secondary
grid = ["__" for i in range(9) ]

def play():
	for i in range(0,9,3):
		print(grid[i]+" "+grid[i+1]+" "+grid[i+2])

turn = True

while "__" in grid:
	play()
	if "__" != grid[0] and grid[0] == grid[4] and grid [4] == grid [8]:
		print(grid[0] +"wins")
	answer = int(input("What space"))
	if answer != 0:
		if turn:
			grid[answer-1] = "x"
		else:
			grid[answer-1] = "o"
		turn = not turn
	else:
		if turn:
			grid = ["x"] *9
		else:
			grid = ["o"] *9
play()