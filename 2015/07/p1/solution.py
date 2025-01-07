def findValue(instructions, wireName):
  wireValues = {}
  ops = {}
  opLookUp = {
    'set': 0,
    'not': 1,
    'and': 2,
    'or': 3,
    'lShift': 4,
    'rShift': 5,
  }
  for instruction in instructions:
    before, after = instruction.split(' -> ')
    parts = before.split(' ')
    if len(parts) == 1:
      if parts[0].isnumeric(): wireValues[parts[0]] = int(parts[0])
      ops[after] = (opLookUp['set'], [parts[0]])
    elif len(parts) == 2:
      if parts[1].isnumeric(): wireValues[parts[1]] = int(parts[1])
      ops[after] = (opLookUp['not'], [parts[1]])
    else:
      if parts[0].isnumeric(): wireValues[parts[0]] = int(parts[0])
      if parts[2].isnumeric(): wireValues[parts[2]] = int(parts[2])

      if parts[1] == 'AND': ops[after] = (opLookUp['and'], [parts[0], parts[2]])
      elif parts[1] == 'OR': ops[after] = (opLookUp['or'], [parts[0], parts[2]])
      elif parts[1] == 'LSHIFT': ops[after] = (opLookUp['lShift'], [parts[0], parts[2]])
      elif parts[1] == 'RSHIFT': ops[after] = (opLookUp['rShift'], [parts[0], parts[2]])
  while len(ops):
    opsToDelete = []
    for op in ops:
      if all([operand in wireValues for operand in ops[op][1]]):
        opsToDelete.append(op)
        if ops[op][0] == opLookUp['set']: wireValues[op] = wireValues[ops[op][1][0]]
        elif ops[op][0] == opLookUp['not']:
          if ~ wireValues[ops[op][1][0]] < 0: wireValues[op] = 65535 + (~ wireValues[ops[op][1][0]]) + 1
          else: wireValues[op] = ~ wireValues[ops[op][1][0]]
        elif ops[op][0] == opLookUp['and']: wireValues[op] = wireValues[ops[op][1][0]] & wireValues[ops[op][1][1]]
        elif ops[op][0] == opLookUp['or']: wireValues[op] = wireValues[ops[op][1][0]] | wireValues[ops[op][1][1]]
        elif ops[op][0] == opLookUp['lShift']: wireValues[op] = wireValues[ops[op][1][0]] << wireValues[ops[op][1][1]]
        elif ops[op][0] == opLookUp['rShift']: wireValues[op] = wireValues[ops[op][1][0]] >> wireValues[ops[op][1][1]]
    for op in opsToDelete:
      del ops[op]
  return 0 if wireName not in wireValues else wireValues[wireName]

def solution(reportLines):
  instructions = [line for line in reportLines]
  print(findValue(instructions, 'a'))
