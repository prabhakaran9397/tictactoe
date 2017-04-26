from random import randint
import os

Grid = [[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]]
Human, Computer = O, X = 'O', 'X'
Current = X
Mode = 0
Winner = "Draw!"

def mode(val):
	global Mode
	Mode = val

def choice(val):
	global Human, Computer
	if val == 'X' or val == 'x':
		Human, Computer = X, O

def booleanize(mat, val):
	bg = [[0 for i in range(3)] for j in range(3)]
	for i in range(3):
		for j in range(3):
			if mat[i][j] == val:
				bg[i][j] = 1
			else:
				bg[i][j] = 0
	return bg

def printGrid():
	os.system('clear')
	print '--------------'
	for row in Grid:
		for i in row:
			if type(i) == int:
				print "", i,
			else:
				print "", "\033[97m{}\033[00m".format(i),
		print
	print '--------------'

def getValHuman(openSet):
	choice = -1
	while choice not in openSet:
		if Current == Human:
			print 'Choose from',
			for i in openSet:
				print i+1,
			print ':',
			choice = input()-1
	return choice

def easyAlgo(openSet):
	return openSet[randint(0, len(openSet)-1)]

def normalAlgo(openSet):
	bH = booleanize(Grid, Human)
	for i in range(3):
		if((~(bH[i][0]^bH[i][1]^bH[i][2]))&(bH[i][0]|bH[i][1]|bH[i][2])):
			for j in range(3):
				if bH[i][j] == 0 and i*3+j in openSet:
					return i*3+j
		if((~(bH[0][i]^bH[1][i]^bH[2][i]))&(bH[0][i]|bH[1][i]|bH[2][i])):
			for j in range(3):
				if bH[j][i] == 0 and j*3+i in openSet:
					return j*3+i

	if((~(bH[0][0]^bH[1][1]^bH[2][2]))&(bH[0][0]|bH[1][1]|bH[2][2])):
			for j in range(3):
				if bH[j][j] == 0 and j*3+j in openSet:
					return j*3+j
	if((~(bH[0][2]^bH[1][1]^bH[2][0]))&(bH[0][2]|bH[1][1]|bH[2][0])):
			for j in range(3):
				if bH[j][2-j] == 0 and j*3+2-j in openSet:
					return j*3+2-j
	return easyAlgo(openSet)

def hardAlgo(openSet):

	bH = booleanize(Grid, Human)
	for i in range(3):
		if((~(bH[i][0]^bH[i][1]^bH[i][2]))&(bH[i][0]|bH[i][1]|bH[i][2])):
			for j in range(3):
				if bH[i][j] == 0 and i*3+j in openSet:
					return i*3+j
		if((~(bH[0][i]^bH[1][i]^bH[2][i]))&(bH[0][i]|bH[1][i]|bH[2][i])):
			for j in range(3):
				if bH[j][i] == 0 and j*3+i in openSet:
					return j*3+i

	if((~(bH[0][0]^bH[1][1]^bH[2][2]))&(bH[0][0]|bH[1][1]|bH[2][2])):
			for j in range(3):
				if bH[j][j] == 0 and j*3+j in openSet:
					return j*3+j
	if((~(bH[0][2]^bH[1][1]^bH[2][0]))&(bH[0][2]|bH[1][1]|bH[2][0])):
			for j in range(3):
				if bH[j][2-j] == 0 and j*3+2-j in openSet:
					return j*3+2-j

	bC = booleanize(Grid, Computer)
	for i in range(3):
		if((bC[i][0]^bC[i][1]^bC[i][2])&(~(bC[i][0]|bC[i][1]|bC[i][2]))):
			for j in range(3):
				if bC[i][j] == 0 and i*3+j in openSet:
					return i*3+j
		if((bC[0][i]^bC[1][i]^bC[2][i])&(~(bC[0][i]|bC[1][i]|bC[2][i]))):
			for j in range(3):
				if bC[j][i] == 0 and j*3+i in openSet:
					return j*3+i

	if((bC[0][0]^bC[1][1]^bC[2][2])&(~(bC[0][0]|bC[1][1]|bC[2][2]))):
			for j in range(3):
				if bC[j][j] == 0 and j*3+j in openSet:
					return j*3+j
	if((bC[0][2]^bC[1][1]^bC[2][0])&(~(bC[0][2]|bC[1][1]|bC[2][0]))):
			for j in range(3):
				if bC[j][2-j] == 0 and j*3+2-j in openSet:
					return j*3+2-j
					
	return easyAlgo(openSet)


def getValComp(openSet):
	Algo = {
		0 : easyAlgo,
		1 : normalAlgo,
		2 : hardAlgo
	}
	print 'Computer has...'
	os.system('sleep 0.5')
	return Algo[Mode](openSet)

def getVal():
	openSet = []
	for i in range(9):
		if type(Grid[i/3][i%3]) == int:
			openSet.append(i)
	
	if Current == Human:
		choice = getValHuman(openSet)
	else:
		choice = getValComp(openSet)

	openSet.remove(choice)
	Grid[choice/3][choice%3] = Current

def checkForWinner():
	global Winner
	bX = booleanize(Grid, X)
	if (
		(bX[0][0]&bX[0][1]&bX[0][2]) | (bX[1][0]&bX[1][1]&bX[1][2]) | (bX[2][0]&bX[2][1]&bX[2][2]) | 
		(bX[0][0]&bX[1][0]&bX[2][0]) | (bX[0][1]&bX[1][1]&bX[2][1]) | (bX[0][2]&bX[1][2]&bX[2][2]) | 
		(bX[0][0]&bX[1][1]&bX[2][2]) | (bX[0][2]&bX[1][1]&bX[2][0])
	   ):
		if Human == X:
			Winner = "You won!"
		else:
			Winner = "Computer won!"
		return False
	bO = booleanize(Grid, O)
	if (
		(bO[0][0]&bO[0][1]&bO[0][2]) | (bO[1][0]&bO[1][1]&bO[1][2]) | (bO[2][0]&bO[2][1]&bO[2][2]) | 
		(bO[0][0]&bO[1][0]&bO[2][0]) | (bO[0][1]&bO[1][1]&bO[2][1]) | (bO[0][2]&bO[1][2]&bO[2][2]) | 
		(bO[0][0]&bO[1][1]&bO[2][2]) | (bO[0][2]&bO[1][1]&bO[2][0])
	   ):
		if Human == O:
			Winner = "You won!"
		else:
			Winner = "Computer won!"
		return False

	for i in range(9):
		if type(Grid[i/3][i%3]) == int:
			return True
	return False


def changeTurn():
	global Current
	if Current == X: Current = O
	else: Current = X	

def main():
	choice(raw_input('X or O? '))
	mode(input('Easy(0) Normal(1) Hard(2): '))
	while checkForWinner():
		printGrid()
		getVal()
		changeTurn()
	printGrid()
	print Winner

if __name__ == '__main__':
	main()