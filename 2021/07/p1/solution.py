import time

def getFuelFor(crabSubs):
	def travelingTo(location):
		return sum([abs(crabSub - location) for crabSub in crabSubs])
	return travelingTo

def getFuelSpent(crabSubs,furthestSub):
	# return min([sum([abs(p - x) for x in locations]) for p in range(maxPos + 1)])
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
	print(getFuelSpent(crabSubs, max(crabSubs)))
	end = time.time()
	print('Time taken = ' + str(end - start))

solution()
