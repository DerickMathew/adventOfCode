def countPossibleAngles(dest):
	xCloser, xFurther, yLower, yHigher = dest
	vals = set()
	for probeStartX in range(xFurther + 1):
		for probeStartY in range(yLower, -yLower):
			probeX, probeY = 0, 0
			velocityX, velocityY = probeStartX, probeStartY
			while probeY >= yLower:
				probeX += velocityX
				probeY += velocityY
				if yLower <= probeY <= yHigher and xCloser <= probeX <= xFurther:
					vals.add((probeStartX, probeStartY))
				velocityY = velocityY - 1
				if probeX > xFurther: break
				if velocityX == 0:
					if probeX < xCloser: break
				else: velocityX -= (velocityX/abs(velocityX))
	return len(vals)

def getHighestPosition(dest):
	xCloser, xFurther, yLower, yHigher = dest
	allTimeHigh = -float('inf')
	hops = len(list(filter(lambda x: x <= xFurther, map(lambda n: (n * (n + 1)) / 2, range(xFurther)))))
	maxProbeHeight = float('inf') * -1
	for probeStartX in range(hops):
		for probeStartY in range(-yLower):
			probeX, probeY = 0, 0
			velocityX, velocityY = probeStartX, probeStartY
			while velocityY >= yLower:
				probeX += velocityX
				probeY += velocityY
				maxProbeHeight = max(maxProbeHeight, probeY)
				if yLower <= probeY <= yHigher and xCloser <= probeX <= xFurther:
					allTimeHigh = max(allTimeHigh, maxProbeHeight)
				velocityY -= 1
				velocityX = 0 if velocityX == 0 else velocityX - (velocityX/abs(velocityX))
	return allTimeHigh

def getXandY(report):
	xRange, yRange =[l.split('=')[1] for l in report.split(': ')[1].split(', ') ]
	[xCloser, xFurther] = [int(n) for n in xRange.split('..')]
	[yLower, yHigher] = [int(n) for n in yRange.split('..')]
	return (xCloser, xFurther, yLower, yHigher)

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('./input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	report = getLinesFromInput()
	part1 = str(getHighestPosition(getXandY(report[0])))
	part2 = str(countPossibleAngles(getXandY(report[0])))
	print ('Part 1:\n' + part1 + '\n')
	print ('Part 2:\n' + part2)

solution()
