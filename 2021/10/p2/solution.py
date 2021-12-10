import time
from functools import reduce

def getClosingScore(line):
	stack = []
	openers = list('([{<')
	closers = list(')]}>')
	for symbol in list(line):
		if symbol in openers:
			stack.append(symbol)
		else:
			if not (openers.index(stack.pop()) == closers.index(symbol)):
				return 0
	stack.reverse()
	return reduce(lambda a, b: a * 5 + b, map(lambda n: openers.index(n) + 1, stack) ,0)

def getMiddleScore(reports):
	closingScore = sorted(list(filter(lambda x: x, map(lambda line: getClosingScore(line), reports))))
	return closingScore[len(closingScore) // 2]

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('../input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	start = time.time()
	report = getLinesFromInput()
	print(getMiddleScore(report))
	end = time.time()
	print('Time taken = ' + str(end - start))

solution()
