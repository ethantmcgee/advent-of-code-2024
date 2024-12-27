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

last_len = len(rules)
while len(rules) > 0:
  rules_to_try_again = []
  for rule in rules:
    if rule[1] in wire_values and rule[2] in wire_values:
      if rule[0] == 0:
        wire_values[rule[3]] = wire_values[rule[1]] & wire_values[rule[2]]
      elif rule[0] == 1:
        wire_values[rule[3]] = wire_values[rule[1]] | wire_values[rule[2]]
      elif rule[0] == 2:
        wire_values[rule[3]] = wire_values[rule[1]] ^ wire_values[rule[2]]
    else:
      rules_to_try_again.append(rule)
  if len(rules_to_try_again) == len(rules):
    rules = []
  else:
    rules = rules_to_try_again

zKeys = sorted([x for x in wire_values.keys() if x[0] == "z"])[::-1]
result = 0
for key in zKeys:
  result |= wire_values[key] << int(key[1:])
print(result)