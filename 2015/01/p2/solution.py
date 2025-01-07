def countFloor(parentheses):
  floor = 0
  for index in range(len(parentheses)):
    floor += 1 if parentheses[index] == '(' else -1
    if floor == -1: return index + 1
  return -1

def solution(reportLines):
  parentheses = [line for line in reportLines]
  print(countFloor(parentheses[0]))
