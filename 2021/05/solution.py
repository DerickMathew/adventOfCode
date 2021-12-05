
def plotPoints(instructions, includeDiagonals = True):
	plotMap = {}
	for line in instructions:
		startStr, endStr = line.split(' -> ')
		[startX, startY] = [int(n) for n in startStr.split(',')]
		[endX, endY] = [int(n) for n in endStr.split(',')]
		if startX == endX:
			markVerticalLines(plotMap, startX, startY, endX, endY)
		elif startY == endY:
			markHorizontalLines(plotMap, startX, startY, endX, endY)
		elif abs(startX-endX) == abs(startY - endY) and includeDiagonals:
			markDiagonalLines(plotMap, startX, startY, endX, endY)
	return plotMap

def incrementKey(pointMap, x, y):
	if (x, y) not in pointMap:
		pointMap[(x, y)] = 0
	pointMap[(x, y)] += 1

def markDiagonalLines(pointMap, startX, startY, endX, endY):
	xIncrement = 1 if startX < endX else -1
	yIncrement = 1 if startY < endY else -1
	for index in range(abs(startX-endX) + 1):
		x = startX + (index * xIncrement)
		y = startY + (index * yIncrement)
		incrementKey(pointMap, x, y)

def markVerticalLines(pointMap, startX, startY, endX, endY):
	for index in range(min(startY, endY), max(startY, endY) + 1 ):
		incrementKey(pointMap, startX, index)

def markHorizontalLines(pointMap, startX, startY, endX, endY):
	for index in range(min(startX, endX), max(startX, endX) + 1 ):
		incrementKey(pointMap, index, startY)

def getOverLap(pointMap):
	return len(list(filter(lambda x: pointMap[x] > 1, pointMap.keys())))

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('./input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	instructions = getLinesFromInput()
	part1 = str(getOverLap(plotPoints(instructions, includeDiagonals = False)))
	part2 = str(getOverLap(plotPoints(instructions)))
	print ('Part 1:\n' + part1 + '\n')
	print ('Part 2:\n' + part2)

solution()
