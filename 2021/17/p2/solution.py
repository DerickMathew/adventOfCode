import time

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

def getXandY(report):
	xRange, yRange =[l.split('=')[1] for l in report.split(': ')[1].split(', ') ]
	[xCloser, xFurther] = [int(n) for n in xRange.split('..')]
	[yLower, yHigher] = [int(n) for n in yRange.split('..')]
	return (xCloser, xFurther, yLower, yHigher)

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('../input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	start = time.time()
	report = getLinesFromInput() 
	print(countPossibleAngles(getXandY(report[0])))
	end = time.time()
	print('Time taken = ' + str(end - start))

solution()
