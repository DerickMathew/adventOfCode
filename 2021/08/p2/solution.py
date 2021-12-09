import time
from itertools import permutations

def getSignalPatternsFor(chars):
	segments = {
		0 : sorted(chars[0] + chars[1] + chars[2] + chars[3] + chars[4] + chars[6]),
		1 : sorted(chars[0] + chars[1]),
		2 : sorted(chars[0] + chars[2] + chars[3] + chars[5] + chars[6]),
		3 : sorted(chars[0] + chars[1] + chars[2] + chars[3] + chars[5]),
		4 : sorted(chars[0] + chars[1] + chars[4] + chars[5]),
		5 : sorted(chars[1] + chars[2] + chars[3] + chars[4] + chars[5]),
		6 : sorted(chars[1] + chars[2] + chars[3] + chars[4] + chars[5] + chars[6]),
		7 : sorted(chars[0] + chars[1] + chars[3]),
		8 : sorted(chars[0] + chars[1] + chars[2] + chars[3] + chars[4] + chars[5] + chars[6]),
		9 : sorted(chars[0] + chars[1] + chars[2] + chars[3] + chars[4] + chars[5])
	}
	return [segments[i] for i in range(10)]

def getSignalPattern (uniquePatterns, allPermutations, signalPatterns):
	for permutation in allPermutations:
		patternPossible = True
		for pattern in uniquePatterns:
			if sorted(pattern) not in signalPatterns[permutation]:
				patternPossible = False
				break
		if patternPossible:
			return signalPatterns[permutation]

def getOutputSum(inputs, outputs):
	allPermutations = [''.join(p) for p in permutations('abcdefg')]
	signalPatterns = {}
	for permutation in allPermutations:
		signalPatterns[permutation] = getSignalPatternsFor(permutation)
	summed = 0
	for i in range(len(outputs)):
		uniqueNumbers = set()
		for pattern in set(outputs[i] + inputs[i]):
			if len(pattern) in [3,4,5]:
				uniqueNumbers.add(''.join(sorted(pattern)))
		pattern = getSignalPattern(uniqueNumbers, allPermutations, signalPatterns)
		summed += int(''.join([str(pattern.index(sorted(signal))) for signal in outputs[i]]), 10)
	return summed

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('../input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	start = time.time()
	report = getLinesFromInput()
	inputs, outputs = [], []
	for line in report:
		inputsStr, outputStr = line.split(' | ')
		inputs.append(inputsStr.split(' '))
		outputs.append(outputStr.split(' '))
	print(getOutputSum(inputs, outputs))
	end = time.time()
	print('Time taken = ' + str(end - start))

solution()
