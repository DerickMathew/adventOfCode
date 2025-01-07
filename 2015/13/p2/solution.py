def findOptimalHappiness(happiness, people):
  totalHappiness = {}
  for person1 in people:
    for person2 in people:
      if person1 != person2 and (person1, person2) not in totalHappiness:
        cost = 0
        if (person1, person2) in happiness: cost += happiness[(person1, person2)]
        if (person2, person1) in happiness: cost += happiness[(person2, person1)]
        totalHappiness[(person1, person2)] = cost
        totalHappiness[(person2, person1)] = cost
  options = [(person , ) for person in people]
  fullTables = []
  while len(options):
    option = options.pop()
    if len(people) == len(option): fullTables.append(option)
    else:
      for person in filter(lambda p: p not in option, people):
        options.append(option + (person ,))
  maxCost = 0
  for chain in fullTables:
    cost = 0
    for index in range(len(chain) - 1):
      cost += totalHappiness[(chain[index], chain[(index + 1)])]
    maxCost = max(maxCost, cost)
  return maxCost

def solution(reportLines):
  happiness = {}
  people = set()
  for line in reportLines:
    text = line.split('.')[0].split(' ')
    object = text[0]
    subject = text[-1]
    people.add(object)
    people.add(subject)
    factor = int(text[3]) 
    factor *= -1 if text[2] == 'lose' else 1
    happiness[(object, subject)] = factor
  print(findOptimalHappiness(happiness, list(people)))
