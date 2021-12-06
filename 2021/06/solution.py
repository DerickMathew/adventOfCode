import time

def getLanternCount(lanternTimer, days):
	lanternCount = [0] * 10
	for i in lanternTimer:
		lanternCount[i] += 1
	for i in range(days):
		newLanternCount = list(map(lambda x: x, lanternCount[1:])) + [0]
		newLanternCount[6] += lanternCount[0]
		newLanternCount[8] += lanternCount[0]
		lanternCount = list(map(lambda x: x, newLanternCount))
	return sum(lanternCount)

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('./input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	instructions = getLinesFromInput()
	lanternTimerCount = [int(n, 10) for n in instructions[0].split(',')]
	part1 = str(getLanternCount(lanternTimerCount, 80))
	part2 = str(getLanternCount(lanternTimerCount, 256))
	print ('Part 1:\n' + part1 + '\n')
	print ('Part 2:\n' + part2)

solution()
