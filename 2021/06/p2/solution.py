import time

def getLanternCount(lanternTimer, days):
	lanternCount = [0] * 10
	for i in lanternTimer:
		lanternCount[i] += 1
	for i in range(days):
		lanternCount[9] = lanternCount[0]
		for i in range(9):
			lanternCount[i] = lanternCount[i+1]
		lanternCount[6] += lanternCount[9]
	return sum(lanternCount[:9])

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('../input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	start = time.time()
	instructions = getLinesFromInput()
	lanternTimerCount = [int(n, 10) for n in instructions[0].split(',')]
	DAYS = 256
	print(getLanternCount(lanternTimerCount, DAYS))
	end = time.time()
	print('Time taken = ' + str(end - start))

solution()
