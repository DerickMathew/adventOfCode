def findTotalRibbonRequired(dimensionOfBoxes):
  ribbonInFeet = 0
  for l, b, w in dimensionOfBoxes:
    ribbonLen = (l * b + b * w + w * l) * 2 
    slack = min(l * b, b * w, w * l)
    ribbonInFeet += (ribbonLen + slack)
  return ribbonInFeet

def solution(reportLines):
  dimensionOfBoxes = [[int(number) for  number in line.split('x')] for line in reportLines]  
  print(findTotalRibbonRequired(dimensionOfBoxes))
