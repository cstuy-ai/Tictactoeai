import time

# || Maze Solving Program||
#
#variables
path = '#'
wall = '='
exit = '$'
visited = '#'
deadend = "."
solved = False
start = '*'
x = 0
y = 1
gamewon = False
#import file
mazefile = open('maze.txt')
#open might read automatically
# file.read () [everything in a string] or file.readlines()[everything in a list] or file.readline()



maze = mazefile.readlines()

'''
we want to turn the  maze file's data into a 2-D list (list of lists).
a list is the python way of saying array (there are some differences but not big
L=  [   [first line], [second line], [third line] ]
		within each of these lines :
			['+', '+', '-' .....]

in order to access an element in each list
(assuming the t
L[0][2]

'''




#maze string array
maze2=[]
for line in maze:
	m=[]
	l=0
	while l < len(line):
		m.append(line[l])
		l += 1
	maze2.append(m)

print maze2[1][0]

def print_maze(maz): #takes a 2 dimensional array and prints it as strings
	print chr(27) +"[2J"	
	for n in maz:
		s=""
		for u in n:
			s += u
		s= s[:-1] #takes out the last character, the extra new linw
		print s


def checkpos(m,r,c):
	global gamewon
	tempmaze = maze2
	if gamewon:
		return
	if maze2[r][c] in "+-|":
		return
	if maze2[r][c] == '$':
		gamewon = True
		return
	if tempmaze[r][c] == '#':
		return
	if tempmaze[r][c] == " ":
		tempmaze[r][c] = '#'
		print_maze(tempmaze)
		time.sleep(0)
		checkpos(tempmaze,r,c+1)
		checkpos(tempmaze,r,c-1)
		checkpos(tempmaze,r+1,c)
		checkpos(tempmaze,r-1,c)
		tempmaze[r][c]="."

checkpos(maze2,1,1)

	


	
	
	
'''
for line in maze:
	s = (line)

for i in m:
	a[x][y] = m[i]
	x += 1
	y += 1
#if it reaches eof breaks out of loop
while(s != None):
	for c in s:
		a[y][x] = c
		x = 0
		s = (line)
'''

'''

st = "fjjklafsdfklasdfkjlsd"
for char in st:
	print char
#Solving Function
#def solve(x,y):
	#if 


'''

	
