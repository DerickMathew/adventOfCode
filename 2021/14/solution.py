def increment(store, key, incrementBy = 1):
	store[key] = store[key] if key in store else 0
	store[key] += incrementBy

def getTemplateAndRules(report):
	template = report[0]
	rules = {}
	for line in report[2:]:
		condition, inserted = line.split(' -> ')
		rules[condition] = inserted
	return template, rules

def getElementDiff(report , steps):
	template, rules = getTemplateAndRules(report)
	letterCount = {}
	list(map(lambda letter: increment(letterCount, letter), template))

	count = {}
	list(map(lambda rule: increment(count, rule, 0), rules))
	possibleKeys = map(lambda i: template[i: i+2], range(len(template) - 1))
	list(map(lambda key: increment(count, key), possibleKeys))
	
	for _ in range(steps):
		list(map(lambda key: increment(letterCount, rules[key], count[key]), count))
		updatedCount = {}
		for key, value in count.items():
			for possibleKey in [key[0]+ rules[key], rules[key] + key[1]]:
				if possibleKey in rules:
					increment(updatedCount, possibleKey, value)
		count = updatedCount
	
	mostAbundant = max(letterCount.values())
	leastAbundant = min(filter(lambda x: not x == 0, letterCount.values()))
	return mostAbundant - leastAbundant

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('./input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	report = getLinesFromInput()
	part1 = str(getElementDiff(report, 10))
	part2 = str(getElementDiff(report, 40))
	print ('Part 1:\n' + part1 + '\n')
	print ('Part 2:\n' + part2)

solution()
