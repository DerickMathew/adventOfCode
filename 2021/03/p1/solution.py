def getPowerConsumption(report):
	gamma, epsilon = 0,0
	wordLen = len(report[0])
	wordCount = len(report)
	for scan in range(wordLen):
		oneCount = len(list(filter(lambda x: x[scan] == '1' , report)))
		zeroCount = wordCount - oneCount
		gamma = gamma * 2 + int(zeroCount >= oneCount)
		epsilon = epsilon * 2 + int(zeroCount <= oneCount)
	return gamma * epsilon

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('../input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	print(getPowerConsumption(getLinesFromInput()))

solution()
