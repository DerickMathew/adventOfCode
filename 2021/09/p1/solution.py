import time

def getLowPointScore(heightMap, h, w):
	neighbors= [(h - 1, w), (h + 1, w), (h, w - 1), (h, w+ 1)]
	for y, x in neighbors:
		if 0 <= y < len(heightMap) and 0 <= x < len(heightMap[0]):
			if heightMap[h][w] >= heightMap[y][x]: return 0
	return 1 + heightMap[h][w]

def getRiskScore(heightMap):
	summed = 0
	for y in range(len(heightMap)):
		for x in range(len(heightMap[0])):
			summed += getLowPointScore(heightMap, y, x)
	return summed

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('../input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	start = time.time()
	report = getLinesFromInput()
	heightMap = list(map( lambda line: [int(x) for x in list(line)], report))
	print(getRiskScore(heightMap))
	end = time.time()
	print('Time taken = ' + str(end - start))

solution()
