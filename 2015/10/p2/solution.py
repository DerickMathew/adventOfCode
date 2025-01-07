def findNumberAfter(strNum, iterations):
  for _ in range(iterations):
    index = 1
    count = 1
    lastChar = strNum[0]
    newNum = ''
    while index < len(strNum):
      if strNum[index] == lastChar: count += 1
      else: 
        newNum += str(count) + strNum[index - 1]
        lastChar = strNum[index]
        count = 1
      index += 1
    newNum += str(count) + strNum[index - 1]
    strNum = newNum
  return len(strNum)

def solution(reportLines):
  strNum = reportLines[0]
  print(findNumberAfter(strNum, 50))
