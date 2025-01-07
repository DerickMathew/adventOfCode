def findMaxPath(paths, locations):
  options = [(location,) for location in locations]
  finalOptions = []
  while len(options):
    path = options.pop()
    if len(path) == len(locations): finalOptions.append(path)
    else:
      remaining = filter(lambda loc: loc not in path, locations)
      for location in remaining:
        options.append(path + (location,))
  maxCost  = 0
  for path in finalOptions:
    cost = sum([paths[(path[i], path[i + 1])] for i in range(len(path) - 1)])
    maxCost = max(maxCost, cost)
  return maxCost

def solution(reportLines):
  paths = {}
  locations = set()
  for line in reportLines:
    parts = line.split(' ')
    start = parts[0]
    end = parts[2]
    distance = int(parts[4])
    locations.add(start)
    locations.add(end)
    paths[(start, end)] = distance
    paths[(end, start)] = distance
  print(findMaxPath(paths, locations))
