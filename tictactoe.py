########################################
# Tic - Tac - Toe Game                 #
# Version 1.0                          #
########################################





# Tic Tac Board Layout |V|
space = " "
board = '''
   |   |   
 %s | %s | %s 
___|___|___
   |   |   
 %s | %s | %s 
___|___|___
   |   |   
 %s | %s | %s 
   |   |   
'''

#print board%(space, space, space, space, space, space, space, space, space)
boardlist = [1,2,3,4,5,6,7,8,9]
print board%tuple(boardlist)
player1 = True


def replace(n, s):
	boardlist[n-1] = s
	return

while True:
	player = "Player 1"
	if player1:
		s = "x"
	else:
		player = "Player 2"
		s = "o"
	inp = input ("Please specify your desired move...\n> ")
	if (inp >= 1 and inp <= 9):
		replace(inp, s)
		player1 = not player1
# If you put in a number that breaks it, returns a message |v|
	else:
		print ("You have specified an invalid number, please choose a number on the board from 1 to 9")

   	print board%tuple(boardlist)

  





