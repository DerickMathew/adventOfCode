def findIncreasingWindow(report, windowSize):
	count = 0
	for i in range(windowSize,len(report)):
		prev = sum(report[i - windowSize: i])
		current = sum(report[i - windowSize + 1: i + 1])
		count += 1 if prev < current else 0
	return count

def getLinesFromInput():
	inputFile = open('../input.txt', 'r') 
	return inputFile.readlines()

def solution():
	inputLines = getLinesFromInput()
	sonarReport = list(map(lambda x:int(x), inputLines))
	windowSize = 3
	print(findIncreasingWindow(sonarReport, windowSize))

solution()
