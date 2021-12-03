def getLocationProduct(instructions):
	x, y = 0, 0
	for instruction in instructions:
		command, valueStr = instruction.split()
		value = int(valueStr)
		if command == 'forward':
			y += value
		elif command == 'down':
			x += value
		else:
			x -= value
	return x * y

def getLinesFromInput():
	inputFile = open('../input.txt', 'r') 
	return inputFile.readlines()

def solution():
	instructions = getLinesFromInput()
	print(getLocationProduct(instructions))

solution()
