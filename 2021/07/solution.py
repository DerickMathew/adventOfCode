def getFuelSpent(crabs,maxCrab):
	return min([sum([abs(l - c) for c in crabs]) for l in range(maxCrab + 1)])

def getFuelSpentIncrementally(crabs,maxCrab):
	sigma = {}
	for n in range(maxCrab + 1):
		sigma[n] = n * (n + 1) // 2
	return min([sum([sigma[abs(l - c)] for c in crabs]) for l in range(maxCrab + 1)])

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('./input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	instructions = getLinesFromInput()
	crabSubs = [int(p) for p in instructions[0].split(',')]
	part1 = str(getFuelSpent(crabSubs, max(crabSubs)))
	part2 = str(getFuelSpentIncrementally(crabSubs, max(crabSubs)))
	print ('Part 1:\n' + part1 + '\n')
	print ('Part 2:\n' + part2)

solution()
