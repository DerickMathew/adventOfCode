
def plotPoints(instructions, includeDiagonals = True):
	plotMap = {}
	for line in instructions:
		startStr, endStr = line.split(' -> ')
		[startX, startY] = [int(n) for n in startStr.split(',')]
		[endX, endY] = [int(n) for n in endStr.split(',')]
		if startX == endX or startY == endY:
			markLines(plotMap, startX, startY, endX, endY)
		elif abs(startX-endX) == abs(startY - endY) and includeDiagonals:
			markLines(plotMap, startX, startY, endX, endY)
	return plotMap

def incrementKey(pointMap, x, y):
	if (x, y) not in pointMap:
		pointMap[(x, y)] = 0
	pointMap[(x, y)] += 1

def getIncrements(start, end):
	if start == end:
		return 0
	if start < end:
		return 1
	return -1

def markLines(pointMap, startX, startY, endX, endY):
	dx = getIncrements(startX, endX)
	dy = getIncrements(startY, endY)
	maxDiff = max(abs(startX-endX),  abs(startY-endY))
	for index in range(maxDiff + 1):
		x = startX + (index * dx)
		y = startY + (index * dy)
		incrementKey(pointMap, x, y)

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
