from functools import cmp_to_key

with open("input.txt") as file:
  lines = [x.strip() for x in file.readlines()]

rules = []
i = 0
while len(lines[i]) > 0:
  rules.append(lines[i].split("|"))
  i += 1

def cmp_items(a, b):
  for rule in rules:
    if a in rule and b in rule:
      if rule.index(a) < rule.index(b):
        return -1
      else:
        return 1
  return 0

sum = 0
for listy in lines[i+1:]:
  parts = listy.split(",")
  good = True
  for rule in rules:
    if rule[0] in parts and rule[1] in parts:
      idx1 = parts.index(rule[0])
      idx2 = parts.index(rule[1])
      if idx1 > idx2:
        good = False
        break
  if not good:
    cmp_items_py3 = cmp_to_key(cmp_items)
    parts.sort(key = cmp_items_py3)
    sum += int(parts[len(parts) // 2])

print(sum)