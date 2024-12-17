with open("input.txt") as file:
  data = [x.strip() for x in file.readlines()]

IP = 0

A = int(data[0].split(": ")[1])
B = int(data[1].split(": ")[1])
C = int(data[2].split(": ")[1])

program = [x for x in map(int, data[4].split(": ")[1].split(","))]

def get_combo(operand):
  if 0 <= operand <= 3:
    return operand
  if operand == 4:
    return A
  if operand == 5:
    return B
  if operand == 6:
    return C
  return 0

output = []
while IP < len(program):
  opcode = program[IP]
  operand = program[IP + 1]
  if opcode == 0:
    A = A // 2**get_combo(operand)
  elif opcode == 1:
    B = B ^ operand
  elif opcode == 2:
    B = get_combo(operand) % 8
  elif opcode == 3:
    if A != 0:
      IP = operand - 2
    else:
      IP += 2
  elif opcode == 4:
    B = B ^ C
  elif opcode == 5:
    output += [str(get_combo(operand) % 8)]
  elif opcode == 6:
    B = A // 2**get_combo(operand)
  elif opcode == 7:
    C = A // 2**get_combo(operand)
  IP += 2

print(",".join(output))