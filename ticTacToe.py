#text-based tic tac toe game for 2 human players
#configuration settings
from tictactoeDefinitions import *
tutorial()
activePlayer = 1

b = 			[" ", " ", " "," ", " ", " "," ", " ", " " ]
clearboard = 	[" ", " ", " "," ", " ", " "," ", " ", " " ]

from IPython.display import clear_output

def display_board(b, lines =5):

    i=0
    rows = [
        [' ', '{} | '.format(str(b[6])), '{}'.format(str(b[7])),' | {}'.format(str(b[8]))],
        [' ', '{} | '.format(str(b[3])), '{}'.format(str(b[4])),' | {}'.format(str(b[5]))],
        [' ', '{} | '.format(str(b[0])), '{}'.format(str(b[1])),' | {}'.format(str(b[2]))] ]
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
test_board = ['#','X','O','X','O','X','O','X','O','X']
clear_output()
display_board(test_board)
# playerOne = input("Player 1: type X or O to select your symbol: ")

# #main game loop, continue executing so long as no one was won
# while not win(): 
# 	makeMove(input("Player "+ str(activePlayer)+ " your move:"))

# 	if win():
# 		break
# 	else:
# 		continue
	
# #If win happens, give option to replay
# again = input("Play again? Y or N: ")

# if again == 'Y':
# 	b = clearboard
# else:
# 	print("Tie tac toe has exited")
	


