import time
from functools import reduce
import random
from sty import fg, bg, ef, rs

colorGuide = {} 
def getNeighbours(x, y):
	return [(y - 1, x), (y + 1, x), (y, x - 1), (y, x+ 1)]

fgs = [fg.da_red, fg.da_blue, fg.da_magenta, fg.black]
bgs = [bg.li_red,bg.red, bg.blue, bg.li_blue, bg.li_magenta, bg.magenta, bg.li_yellow, bg.li_cyan, bg.grey, bg.white]

def getBasinSize(heightMap, h, w):
	neighbors= getNeighbours(w, h)
	for y, x in neighbors:
		if 0 <= y < len(heightMap) and 0 <= x < len(heightMap[0]):
			if heightMap[h][w] >= heightMap[y][x]:
				return 0
	basin = [(h, w)]
	size = 0
	currentColor = fgs[random.randrange(len(fgs))] + bgs[random.randrange(len(bgs))]
	while len(basin):
		y, x = basin.pop()
		currentPoint = heightMap[y][x]
		if not 9 == currentPoint: # handle points that were acted on after being added
			size += 1
			neighbors = getNeighbours(x, y)
			heightMap[y][x] = 9
			colorGuide[(x, y)] = currentColor
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

def getColoredMapText(text, color=None):
	text = ' ' if text == '9' else text
	color = fg.black if not color else color
	return color + text + fg.rs + bg.rs

def prettyPrintMap(heightMap):
	print('\n'*10)
	for y in range(len(heightMap)):
		print(' ' * 20, end='')
		for x in range(len(heightMap[0])):
			color = colorGuide[(x,y)] if (x, y) in colorGuide else None
			print(getColoredMapText(str(heightMap[y][x]) , color), end ='')
		print()
	print('\n'*5)

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('./input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	report = getLinesFromInput()
	heightMap = list(map( lambda line: [int(x) for x in list(line)], report))
	for y in range(len(heightMap)):
		for x in range(len(heightMap[0])):
			if heightMap[y][x] == 9:
				pass
				# colorGuide[(x, y)] = fg.black + bg.black
	getProductOf3LargestBasins(heightMap)
	prettyPrintMap(heightMap)

solution()
