import sys
sys.dont_write_bytecode = True

import os
from time import time
from p1.solution import solution as part1
from p2.solution import solution as part2

def getInputFromFile(fileName):
  inputFile = open(fileName, 'r')
  return [x.rstrip() for x in inputFile.readlines()]

def getFileNames(isTesting, part):
  if not isTesting:
    return['./input.txt']
  parentFolder = './p' + str(part) +'/tests'
  fileNames = filter(lambda file: file.endswith('.txt'), os.listdir(parentFolder))
  return list(map(lambda name:  parentFolder + '/' + name, fileNames))

def executeSolution(isTesting, parts):
  for part in parts:
    for fileName in getFileNames(isTesting, part):
      inputLines = getInputFromFile(fileName)
      execute = part1 if part == 1 else part2
      print('\nPart ', part, ', Input file', fileName)
      start = time()
      execute(inputLines)
      end = time()
      print('Time : ', end - start, 's')

def main():
  isTesting = False
  # partsToRun = [1]
  partsToRun = [1, 2]
  executeSolution(isTesting, partsToRun)

if __name__=="__main__": 
  main() 
