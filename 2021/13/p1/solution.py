import time

def plotHoles(holes):
	maxY = max(map(lambda point: point[0], holes)) + 1
	maxX = max(map(lambda point: point[1], holes)) + 1
	print('\n')
	for y in range(maxY):
		line = ['#' if (y, x) in holes else ' ' for x in range(maxX)]
		print(''.join(line))
	print('\n')

def getHolesAndFolds(instructions):
	holes, folds = [], []
	for line in instructions:
		if ',' in line:
			x, y = line.split(',')
			holes.append((int(y), int(x)))
		elif '=' in line:
			axis, mid = line.split('=')
			folds.append((axis[-1], int(mid)))
	return holes, folds

def foldPoint(point, midPoint):
	if point < midPoint:
		return point	
	return (midPoint * 2) - point

def foldPoints(points, midPoint):
	return list (map(lambda point: foldPoint(point, midPoint), points))

def getNewPoints(points, axis, midPoint):
	Ys = [y for y, x in points]
	Xs = [x for y, x in points]
	if axis == 'y':
		Ys = foldPoints(Ys, midPoint)
	else:
		Xs = foldPoints(Xs, midPoint)
	return list(set([(Ys[i], Xs[i]) for i in range(len(Ys))]))

def countRoutes(instructions):
	holes, folds = getHolesAndFolds(instructions)
	axis, midPoint = folds[0]
	return len(getNewPoints(holes, axis, midPoint))

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('../input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	start = time.time()
	report = getLinesFromInput()
	print(countRoutes(report))
	end = time.time()
	print('Time taken = ' + str(end - start))

solution()
