#tic tac toe
import secondary

grid = ["__" for i in range(9)]


def play():
  for i in range(0, 9, 3):
    print(grid[i] + " " + grid[i + 1] + " " + grid[i + 2])


turn = True

while "__" in grid:
	play()
	if ("__" != grid[0] and grid[0] == grid[4] and grid[4] == grid[8]) or ("__" != grid[2] and grid[2] == grid[4] and grid[4] == grid[6]) or ("__" != grid[0] and grid[0] == grid[1] and grid[1] == grid[2]) or ("__" != grid[3] and grid[3] == grid[4] and grid[4] == grid[5]) or ("__" != grid[6] and grid[6] == grid[7]and grid[7] == grid[8]):
		print(grid[0] + " wins")
		quit()
	answer = int(input("What space\n>"))
	if answer != 0:
		if grid[answer] == "__":
			if turn:
				grid[answer - 1] = "x"
			else:
				grid[answer - 1] = "o"
		turn = not turn
	else:
		if turn:
			grid = ["x"] * 9
			play()
			print("x wins")
			quit()
    else:
      grid = ["o"] * 9
      play()
      print("o wins")
      quit()
play()
print("Tie")
