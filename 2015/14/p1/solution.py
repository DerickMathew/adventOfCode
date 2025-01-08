def getFurthestDistance(reindeer, raceTime):
  maxDistance = 0
  for speed, time, rest in reindeer:
    distance = speed * time * (raceTime // (time + rest))
    remainingTime = (raceTime % (time + rest))
    if remainingTime >= time: distance += (speed * time)
    else: distance += (speed * remainingTime)
    maxDistance = max(distance, maxDistance)
  return maxDistance

def solution(reportLines):
  reindeer = []
  for line in reportLines:
    parts = line.split(' ')
    speed = int(parts[3])
    time = int(parts[6])
    rest = int(parts[13])
    reindeer.append((speed, time, rest))
  print(getFurthestDistance(reindeer, 2503))
