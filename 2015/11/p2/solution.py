alphabet = 'abcdefghijklmnopqrstuvwxyz'

def isValidNumericPassword(password):
  iIndex = alphabet.index('i')
  lIndex = alphabet.index('l')
  oIndex = alphabet.index('o')
  if iIndex in password: return False
  if lIndex in password: return False
  if oIndex in password: return False
  pairs = []
  for i in range(len(password) - 1):
    if password[i] == password[i+1]: pairs.append(i)

  hasRun = False
  for i in range(len(password) - 2):
    if password[i + 1] - password[i] == 1:
      if password[i + 2] - password[i + 1] == 1: hasRun = True

  if not hasRun: return False
  if len(pairs) < 2: return False
  if len(pairs) == 2 and abs(pairs[0] - pairs[1]) == 1: return False
  return True

def getNextNumericPassword(password):
  changed = False
  iIndex = alphabet.index('i')
  lIndex = alphabet.index('l')
  oIndex = alphabet.index('o')
  nextPassword = password[:]
  for i in range(len(password)):
    if not changed: 
      if password[i] in [iIndex, oIndex, lIndex]:
        password[i] = password[i] + 1
        changed = True
    else: password[i] = 0
  changed = False
  for i in range(len(password) - 1, -1, -1):
    if not changed: 
      if password[i] < alphabet.index('z'):
        password[i] = password[i] + 1
        changed = True
      else: password[i] = 0
  return password

def getStringPassword(password):
  return ''.join([alphabet[i] for i in password])

def getNumericPassword(password):
  return [alphabet.index(c) for c in password]

def getNextValidPassword(password):
  numericPassword = getNumericPassword(password)
  numericPassword = getNextNumericPassword(numericPassword)
  while not isValidNumericPassword(numericPassword):
    numericPassword = getNextNumericPassword(numericPassword)
  return getStringPassword(numericPassword)

def solution(reportLines):
  currentPassword = reportLines[0]
  print(getNextValidPassword(currentPassword))
