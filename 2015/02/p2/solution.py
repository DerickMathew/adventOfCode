def findTotalRibbonRequired(dimensionOfBoxes):
  ribbonInFeet = 0
  for l, b, w in dimensionOfBoxes:
    ribbonLen = (l + b + w - max(l, b, w)) * 2
    bowLen = l * b * w
    ribbonInFeet += (ribbonLen + bowLen)
  return ribbonInFeet

def solution(reportLines):
  dimensionOfBoxes = [[int(number) for  number in line.split('x')] for line in reportLines]  
  print(findTotalRibbonRequired(dimensionOfBoxes))
