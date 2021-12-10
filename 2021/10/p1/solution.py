import time

def getScoreByBracket(bracket):
	score = {
		')':3,
		']':57,
		'}':1197,
		'>':25137
	}
	return score[bracket] if bracket in score else 0

def getErrorScore(line):
	stack = []
	openers = list('([{<')
	closers = list(')]}>')
	for symbol in list(line):
		if symbol in openers:
			stack.append(symbol)
		else:
			if not (openers.index(stack.pop()) == closers.index(symbol)):
				return getScoreByBracket(symbol)
	return 0

def getTotalScore(reports):
	return sum(map(lambda line: getErrorScore(line), reports))

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('../input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	start = time.time()
	report = getLinesFromInput()
	print(getTotalScore(report))
	end = time.time()
	print('Time taken = ' + str(end - start))

solution()
