def findLitCount(instructions):
  lights = {}
  for i in range(1000):
    for j in range(1000):
      lights[(i, j)] = 0
  for instruction in instructions:
    parts = instruction.split(',')
    op = 0 # turn off
    if instruction[:len('turn on')] == 'turn on': op = 1
    if instruction[:len('toggle')] == 'toggle': op = 2
    startX = int(parts[0].split(' ')[-1])
    startY = int(parts[1].split(' ')[0])
    endX = int(parts[1].split(' ')[-1])
    endY = int(parts[2])
    for i in range(startX, endX + 1):
      for j in range(startY, endY + 1):
        if op == 0: lights[(i, j)] = max(0, lights[(i, j)] - 1)
        elif op == 1: lights[(i, j)] += 1
        else: lights[(i, j)] += 2
  count = 0
  for i in range(1000):
    for j in range(1000):
      count += lights[(i, j)]
  return count

def solution(reportLines):
  instructions = [line for line in reportLines]
  print(findLitCount(instructions))
