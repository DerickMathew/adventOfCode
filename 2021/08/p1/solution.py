import time

def getUniqueSignalCount(outputs):
	numFromLen = {
		2: 1,
		3: 7,
		4: 4,
		7: 8
	}
	return len(list(filter(lambda chars: len(chars) in numFromLen, outputs)))

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('../input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	start = time.time()
	report = getLinesFromInput()
	outputs = []
	for line in report:
		outputs += line.split(' | ')[1].split(' ')
	print(getUniqueSignalCount(outputs))
	end = time.time()
	print('Time taken = ' + str(end - start))

solution()
