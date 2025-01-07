import hashlib

def findZerosHash(startingString, zeroCount):
  i = 0
  expectedStart = '0' * zeroCount
  while True:
    if i > 0 and i % 1000000000 == 0: input("Waiting...")
    text = startingString + str(i)
    m = hashlib.md5()
    m.update(text.encode('UTF-8'))
    if m.hexdigest()[:zeroCount] == expectedStart: return i
    i += 1

def solution(reportLines):
  startingString = reportLines[0]
  print(findZerosHash(startingString, 6))
