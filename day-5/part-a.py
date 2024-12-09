with open("input.txt") as file:
  lines = [x.strip() for x in file.readlines()]

rules = []
i = 0
while len(lines[i]) > 0:
  rules.append(lines[i].split("|"))
  i += 1

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
  if good:
    sum += int(parts[len(parts) // 2])

print(sum)