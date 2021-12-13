import time

def countRoutes(graph, current, visited):
	if current == 'end':
		return 1
	options = list(filter(lambda x: x not in visited, graph[current]))
	if current.islower():
		visited = set(list(visited) + [current])
	return sum(map(lambda option: countRoutes(graph, option, visited), options))

def appendConnection(graph, node, connectedTo):
	if node not in graph:
		graph[node] = []
	graph[node].append(connectedTo)

def getLinesFromInput(removeTrailingNewLines = True):
	inputFile = open('../input.txt', 'r') 
	if removeTrailingNewLines:
		return list(map(lambda x: x.rstrip('\n'), inputFile.readlines()))
	return inputFile.readlines()

def solution():
	start = time.time()
	report = getLinesFromInput()
	graph = {}
	for line in report:
		src, dest = line.split('-')
		appendConnection(graph, src, dest)
		appendConnection(graph, dest, src)
	print(countRoutes(graph, 'start', set()))
	end = time.time()
	print('Time taken = ' + str(end - start))

solution()
