def findCharDifference(string):
  actualLen = len(string)
  calculatedLen = 0
  # remove double quotes
  index = 1
  while index < len(string) - 1:
    if string[index] != '\\': index += 1
    else:
      index += 1
      if string[index] == '\\': index += 1
      elif string[index] == '"': index += 1
      elif string[index] == 'x': index += 3
    calculatedLen += 1    
  return actualLen - calculatedLen

def findAllCharDifferences(strings):
  return sum([findCharDifference(string) for string in strings])

def solution(reportLines):
  strings = [line for line in reportLines]
  print(findAllCharDifferences(strings))
