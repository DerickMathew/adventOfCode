def isNice(string):
  vowelCount = sum([1 if c in 'aeiou' else 0 for c in string])
  if vowelCount < 3: return False
  hasRepeat = False
  for i in range(len(string) - 1):
    hasRepeat = hasRepeat or (string[i] == string[i+1])
    if string[i:i+2] in ['ab', 'cd', 'pq', 'xy']: return False
  return hasRepeat

def getNiceStringCount(strings):
  return sum([1 if isNice(string) else 0 for string in strings])

def solution(reportLines):
  strings = [line for line in reportLines]
  print(getNiceStringCount(strings))
