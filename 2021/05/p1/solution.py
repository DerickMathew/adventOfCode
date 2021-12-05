def markboard(instructions):
	m = {}
	for line in instructions:
		startStr, endStr = line.split(' -> ')
		[startX, startY] = [int(n) for n in startStr.split(',')]
		[endX, endY] = [int(n) for n in endStr.split(',')]
		if startX == endX:
			markVerticalLines(startX, startY, endX, endY, m)
		if startY == endY:
			markHorizontalLines(startX, startY, endX, endY, m)
	return m

def markVerticalLines(startX, startY, endX, endY, marked):
	for index in range(min(startY, endY), max(startY, endY) + 1 ):
		if (startX, index) not in marked:
			marked[(startX, index)] = 0
		marked[(startX, index)] += 1

def markHorizontalLines(startX, startY, endX, endY, marked):
	for index in range(min(startX, endX), max(startX, endX) + 1 ):
		if (index, startY) not in marked:
			marked[(index, startY)] = 0
		marked[(index, startY)] += 1

def getOverLap(pointMap):
	return len(list(filter(lambda x: pointMap[x] > 1, pointMap.keys())))

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('../input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	instructions = getLinesFromInput()
	ptMap = markboard(instructions)
	print(getOverLap(ptMap))

solution()
