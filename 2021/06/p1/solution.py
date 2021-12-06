import time

def getLanternCount(lanternTimer, days):
	for i in range(days):
		newLanterns = []
		for lantern in lanternTimer:
			if lantern == 0:
				newLanterns.append(8)
				lantern = 7
			newLanterns.append(lantern - 1)
		lanternTimer = newLanterns
	return len(lanternTimer)

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('../input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	start = time.time()
	instructions = getLinesFromInput()
	lanternTimerCount = [int(n, 10) for n in instructions[0].split(',')]
	DAYS = 80
	print(getLanternCount(lanternTimerCount, DAYS))
	end = time.time()
	print('Time taken = ' + str(end - start))

solution()