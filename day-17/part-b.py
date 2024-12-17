with open("input.txt") as file:
  data = [x.strip() for x in file.readlines()]

program = [x for x in map(int, data[4].split(": ")[1].split(","))]

def get_combo(operand, A, B, C):
  if 0 <= operand <= 3:
    return operand
  if operand == 4:
    return A
  if operand == 5:
    return B
  if operand == 6:
    return C
  return 0

def compute(A, B, C):
  IP = 0
  output = []
  while IP < len(program):
    opcode = program[IP]
    operand = program[IP + 1]
    if opcode == 0:
      A = A // 2**get_combo(operand, A, B, C)
    elif opcode == 1:
      B = B ^ operand
    elif opcode == 2:
      B = get_combo(operand, A, B, C) % 8
    elif opcode == 3:
      if A != 0:
        IP = operand - 2
      else:
        IP += 2
    elif opcode == 4:
      B = B ^ C
    elif opcode == 5:
      output += [get_combo(operand, A, B, C) % 8]
    elif opcode == 6:
      B = A // 2**get_combo(operand, A, B, C)
    elif opcode == 7:
      C = A // 2**get_combo(operand, A, B, C)
    IP += 2
  return output

def solve(n, pos):
  res = [1E20]
  if pos == -1:
    return n
  for i in range(8):
      a = n + i * 8**pos
      output = compute(a, 0, 0)
      if len(output) != len(program):
        continue
      if output[pos] == program[pos]:
        res.append(solve(a, pos - 1))
  return min(res)

print(solve(0, len(program) - 1))