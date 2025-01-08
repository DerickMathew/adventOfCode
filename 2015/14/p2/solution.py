def getFurthestDistance(reindeer, raceTime):
  distances = {}
  scores = {}
  for i in range(len(reindeer)):
    distances[i] = 0
    scores[i] = 0
  for t in range(raceTime):
    for i in range(len(reindeer)):
      speed, time, rest = reindeer[i]
      if (t % (time + rest)) < time:
        distances[i] += speed
    maxDistance = max(distances.values())
    for i in range(len(reindeer)):
      if distances[i] == maxDistance: scores[i] += 1
  return max(scores.values())

def solution(reportLines):
  reindeer = []
  for line in reportLines:
    parts = line.split(' ')
    speed = int(parts[3])
    time = int(parts[6])
    rest = int(parts[13])
    reindeer.append((speed, time, rest))
  print(getFurthestDistance(reindeer, 2503))
