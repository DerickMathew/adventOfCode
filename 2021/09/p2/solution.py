import time
from functools import reduce

def getNeighbours(x, y):
	return [(y - 1, x), (y + 1, x), (y, x - 1), (y, x+ 1)]

def getBasinSize(heightMap, h, w):
	neighbors= getNeighbours(w, h)
	for y, x in neighbors:
		if 0 <= y < len(heightMap) and 0 <= x < len(heightMap[0]):
			if heightMap[h][w] >= heightMap[y][x]:
				return 0
	basin = [(h, w)]
	size = 0
	while len(basin):
		y, x = basin.pop()
		currentPoint = heightMap[y][x]
		if not 9 == currentPoint: # handle points that were acted on after being added
			size += 1
			neighbors = getNeighbours(x, y)
			heightMap[y][x] = 9
			for nY, nX in neighbors:
				if 0 <= nY < len(heightMap) and 0 <= nX < len(heightMap[0]):
					if currentPoint <= heightMap[nY][nX] < 9:
						basin.append((nY, nX))
	return size

def getProductOf3LargestBasins(heightMap):
	basinSize = []
	for y in range(len(heightMap)):
		for x in range(len(heightMap[0])):
			basinSize.append(getBasinSize(heightMap, y, x))
	basinSize.sort()
	prod = reduce(lambda a,b: a*b, basinSize[-3:], 1)
	return prod

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('../input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	start = time.time()
	report = getLinesFromInput()
	heightMap = list(map( lambda line: [int(x) for x in list(line)], report))
	print(getProductOf3LargestBasins(heightMap))
	end = time.time()
	print('Time taken = ' + str(end - start))

solution()
