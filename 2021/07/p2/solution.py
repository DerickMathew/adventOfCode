import time

sigma = {}

def populateSigmaTo(largestValue):
	for n in range(largestValue + 1):
		sigma[n] = n * (n + 1) // 2

def getFuelFor(crabSubs: list()):
	def travelingTo(location: int):
		return sum([sigma[abs(crabSub - location)] for crabSub in crabSubs])
	return travelingTo

def getFuelSpent(crabSubs,furthestSub):
	# return min([sum([sigma[abs(p - x)] for x in crabSubs]) for p in range(furthestSub + 1)])
	getFuelTo = getFuelFor(crabSubs)
	return min([getFuelTo(location) for location in range(furthestSub + 1)])

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('../input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	start = time.time()
	report = getLinesFromInput()
	crabSubs = [int(p) for p in report[0].split(',')]
	furthestCrab = max(crabSubs)
	populateSigmaTo(furthestCrab)
	print(getFuelSpent(crabSubs, furthestCrab))
	end = time.time()
	print('Time taken = ' + str(end - start))

solution()
