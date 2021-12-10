from functools import reduce

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
	inputFile = open('./input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	report = getLinesFromInput()
	part1 = str(getTotalScore(report))
	part2 = str(getMiddleScore(report))
	print ('Part 1:\n' + part1 + '\n')
	print ('Part 2:\n' + part2)

solution()
