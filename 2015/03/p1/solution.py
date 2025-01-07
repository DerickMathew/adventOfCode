def getVisitedHouseCount(directions):
  visited = set()
  x, y = 0, 0
  visited.add((x, y))
  for direction in directions:
    if direction == '^': y -= 1
    elif direction == 'v': y += 1
    elif direction == '<': x -= 1
    elif direction == '>': x += 1
    visited.add((x, y))
  return len(visited)

def solution(reportLines):
  directions = [line for line in reportLines]
  print(getVisitedHouseCount(directions[0]))
