def findExpandedCharDifference(string):
  actualLen = len(string)
  calculatedLen = 0
  # remove double quotes
  index = 0
  calculatedLen += 2
  while index < len(string):
    if string[index] == '"': calculatedLen += 2
    elif string[index] == '\\': calculatedLen += 2
    else: calculatedLen += 1
    index += 1
  return calculatedLen - actualLen

def findAllCharDifferences(strings):
  return sum([findExpandedCharDifference(string) for string in strings])

def solution(reportLines):
  strings = [line for line in reportLines]
  print(findAllCharDifferences(strings))
