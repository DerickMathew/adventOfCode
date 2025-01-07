def getNewPosition(x, y, direction):
  if direction == '^': y -= 1
  elif direction == 'v': y += 1
  elif direction == '<': x -= 1
  elif direction == '>': x += 1
  return x, y

def getVisitedHouseCount(directions):
  visited = set()
  sx, sy = 0, 0
  rx, ry = 0, 0
  visited.add((sx, sy))
  for index in range(len(directions)):
    direction = directions[index]
    if index % 2:
      sx, sy = getNewPosition(sx, sy, direction)
      visited.add((sx, sy))
    else:
      rx, ry = getNewPosition(rx, ry, direction)
      visited.add((rx, ry))
  return len(visited)

def solution(reportLines):
  directions = [line for line in reportLines]
  print(getVisitedHouseCount(directions[0]))
