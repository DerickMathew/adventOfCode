def getLocationProduct(instructions):
	x, y, aim = 0, 0, 0
	for instruction in instructions:
		command, valueStr = instruction.split()
		value = int(valueStr)
		if command == 'forward':
			y += value
			x += (aim * value)
		elif command == 'down':
			aim += value
		else:
			aim -= value
	return x * y

def getLinesFromInput():
	inputFile = open('../input.txt', 'r') 
	return inputFile.readlines()

def solution():
	instructions = getLinesFromInput()
	print(getLocationProduct(instructions))

solution()
