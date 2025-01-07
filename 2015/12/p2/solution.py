import json

def findSumOfNumbers(jsonStr):
  count = 0
  jsonObj = json.loads(jsonStr)
  options = [jsonObj]
  while len(options):
    option = options.pop()
    if isinstance(option, int): count += option
    elif isinstance(option, list):
      for i in option:
        options.append(i)
    elif isinstance(option, dict):
      hasRed = False
      for key in option.keys():
        if option[key] == 'red': hasRed = True
      if not hasRed:
        for key in option.keys(): options.append(option[key])
  return count

def solution(reportLines):
  jsonStr = reportLines[0]
  print(findSumOfNumbers(jsonStr))
