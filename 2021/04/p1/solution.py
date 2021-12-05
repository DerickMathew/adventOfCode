def getBoards(instructions):
	boards = []
	i = 2
	while i < len(instructions):
		board = []
		for line in instructions[i: i+5]:
			board.append([int(n) for n in line.split()])
		boards.append(board)
		i+=6
	return boards

def isBoardWinner(board):
	if not hasSelectedLine(board):
		spunBoard = list(map(list, zip(*board)))
		return hasSelectedLine(spunBoard)
	return True
	
def hasSelectedLine(board):
	return any(map(lambda line: sum(line) == 0, board))

def markBoards(calledNumber, boards):
	BOARD_SIZE = 5
	for boardIndex in range(len(boards)):
		for lineIndex in range(BOARD_SIZE):
			for numIndex in range(BOARD_SIZE):
				if boards[boardIndex][lineIndex][numIndex] == calledNumber:
					boards[boardIndex][lineIndex][numIndex] = 0
	return boards

def getWinningScore(calledNumbers, boards):
	for number in calledNumbers:
		for board in markBoards(number, boards):
			if isBoardWinner(board):
				unmarkedSum = sum([sum(line) for line in board])
				return unmarkedSum * number
	return 'The givens have changed, son'

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('../input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	instructions = getLinesFromInput()
	calledNumbers = [int(x) for x in instructions[0].split(',')]
	boards = getBoards(instructions)
	print(getWinningScore(calledNumbers, boards))

solution()
