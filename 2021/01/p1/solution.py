def findIncreases(numbers):
	count = 0
	for i in range(1, len(numbers)):
		count += 1 if numbers[i - 1] < numbers[i] else 0
	return count

def getLinesFromInput():
	inputFile = open('../input.txt', 'r') 
	return inputFile.readlines()

def solution():
	reportLines = getLinesFromInput()
	numbersInReport = list(map(lambda x:int(x), reportLines))
	print(findIncreases(numbersInReport))

solution()
