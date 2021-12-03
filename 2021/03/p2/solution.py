def getRating(report, bitCriteria):
	index = 0
	while(len(report) > 1):
		zeros = list(filter(lambda l: l[index] == '0', report))
		ones = list(filter(lambda l: l[index] == '1', report))
		report = bitCriteria(zeros, ones)
		index += 1
	return int(''.join(report[0]), 2)

def oxygenCriteria(zeros, ones):
	return ones if len(ones) >= len(zeros) else zeros

def carbonDiOxideCriteria(zeros, ones):
	return zeros if len(zeros) <= len(ones) else ones

def getLifeSupportRating(report):
	oxygenRating = getRating(report, oxygenCriteria)
	carbonDiOxideRating = getRating(report, carbonDiOxideCriteria)
	return oxygenRating * carbonDiOxideRating

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('../input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	reportLines = getLinesFromInput()
	print(str(getLifeSupportRating(reportLines)))

solution()
