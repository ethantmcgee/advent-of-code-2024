from collections import defaultdict

with open("input.txt") as file:
  lines = [x.strip() for x in file.readlines()]

wire_values = {}
rules = []
i = 0
for line in lines:
  if line == "":
    break
  wire, value = line.split(": ")
  wire_values[wire] = int(value)
  i += 1

for line in lines[i + 1:]:
  rule, out = line.split(" -> ")
  if " AND " in rule:
    rules.append((0, rule.split(" AND ")[0], rule.split(" AND ")[1], out))
  elif " OR " in rule:
    rules.append((1, rule.split(" OR ")[0], rule.split(" OR ")[1], out))
  elif " XOR " in rule:
    rules.append((2, rule.split(" XOR ")[0], rule.split(" XOR ")[1], out))

chain = defaultdict(list)
for op, op1, op2, out in rules:
  chain[op1].append((op, out))
  chain[op2].append((op, out))

invalid = set()
for op, op1, op2, out in rules:
  has_chained_xor = any([x[0] == 2 for x in chain[out]])
  has_chained_and = any([x[0] == 0 for x in chain[out]])
  has_chained_or = any([x[0] == 1 for x in chain[out]])
  
  takes_first_input = op1.endswith("00") and op2.endswith("00")
  takes_input_bit = (op1.startswith('x') and op2.startswith('y')) or (op2.startswith('x') and op1.startswith('y'))
  outputs_bit = out.startswith('z')
  outputs_last_bit = out == "z45"

  valid = False
  if op == 2:
    valid = ((not takes_input_bit) and outputs_bit) or (takes_input_bit and has_chained_xor) or (takes_first_input and outputs_bit)
  elif op == 1:
    valid = outputs_last_bit or (has_chained_and and has_chained_xor)
  elif op == 0:
    valid = has_chained_or or takes_first_input

  if not valid:
    invalid.add(out)

print(",".join(sorted(invalid)))
