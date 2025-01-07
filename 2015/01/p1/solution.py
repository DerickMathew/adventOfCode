def countFloor(parentheses):
  floor = 0
  for parenthesis in parentheses:
    if parenthesis == '(': floor += 1
    elif parenthesis == ')': floor -= 1
  return floor

def solution(reportLines):
  parentheses = [line for line in reportLines]
  print(countFloor(parentheses[0]))
