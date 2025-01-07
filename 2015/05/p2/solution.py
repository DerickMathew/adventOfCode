def isNice(string):
  hasNonOverlappingRepeat = False
  pairs = {}
  for i in range(len(string) - 1):
    if string[i:i+2] not in pairs: pairs[string[i:i+2]] = i
    elif pairs[string[i:i+2]] != i-1: hasNonOverlappingRepeat = True
  hasSpacedRepeat = False
  for i in range(len(string) - 2):
    hasSpacedRepeat = hasSpacedRepeat or string[i] == string[i+2]
  return hasNonOverlappingRepeat and hasSpacedRepeat

def getNiceStringCount(strings):
  return sum([1 if isNice(string) else 0 for string in strings])

def solution(reportLines):
  strings = [line for line in reportLines]
  print(getNiceStringCount(strings))
