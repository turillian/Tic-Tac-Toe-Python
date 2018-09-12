

# prints the tutorial for the game
def tutorial():
	print('Each of the numbers 1 through 9 represents one space on the board')
	print('Player 1 goes first')

	return True

# map keyboard number to board position (0 1 2) x (0 1 2)
def makeMove(num,board):
	
	print(num2Array[num])
	pass


def win():
	# if True #b[0]#if win condition goes here():
	# 	return True
	# #else:
	pass	



def printBoard(b,lines=5):
	i=0
	rows = [
		[' ', '{} | '.format(str(b[7])), '{}'.format(str(b[8])),' | {}'.format(str(b[9]))],
		[' ', '{} | '.format(str(b[4])), '{}'.format(str(b[5])),' | {}'.format(str(b[6]))],
		[' ', '{} | '.format(str(b[1])), '{}'.format(str(b[2])),' | {}'.format(str(b[3]))] ]
	#Builds the b one line at a time, 
	#Even lines are the horizontal dividers ex: ---------, 
	#Odd lines contain | and the states from b, ex: | X |  
	while lines > 0:

		if lines%2 == 0:
			print("-----------")
		else:
			#iterates over row i and joins all the strings
			print("".join(rows[i]))
			i += 1
		lines -= 1
	pass



