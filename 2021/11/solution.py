def getNeighbours(y, x):
	neighbours = []
	for nY in range(y - 1, y + 2):
		for nX in range(x - 1, x + 2):
			if not (nY == y and nX == x):
				neighbours.append((nY, nX))
	return neighbours

def getStepsToSuperFlash(octos):
	flashCount = steps = 0
	octoCount = len(octos)
	stack = list(octos.keys())
	while not flashCount == octoCount:
		flashCount = 0
		while len(stack):
			y, x = stack.pop()
			octos[(y,x)] += 1
			if octos[(y,x)] == 10:
				for neighbour in getNeighbours(y, x):
					if neighbour in octos:
						stack.append(neighbour)
		for key in octos:
			stack.append(key)
			if octos[key] > 9:
				flashCount += 1
				octos[key] = 0
		steps += 1
	return steps
	
def countFlashes(octos, steps):
	flashCount = 0
	stack = list(octos.keys())
	for _ in range(steps):
		while len(stack):
			y, x = stack.pop()
			octos[(y,x)] += 1
			if octos[(y,x)] == 10:
				for neighbour in getNeighbours(y, x):
					if neighbour in octos:
						stack.append(neighbour)
		for key in octos.keys():
			stack.append(key)
			if octos[key] > 9:
				flashCount += 1
				octos[key] = 0
	return flashCount

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('./input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	report = getLinesFromInput()
	octos = {}
	for y in range(len(report)):
		for x in range(len(report[y])):
			octos[(y,x)] = int(report[y][x])
	part1 = str(countFlashes(octos, 100))
	part2 = str(getStepsToSuperFlash(octos))
	print ('Part 1:\n' + part1 + '\n')
	print ('Part 2:\n' + part2)

solution()
