with open("input.txt") as file:
  lines = [x.strip() for x in file.readlines()]

def safe_get(x, y):
  if 0 <= x < len(lines) and 0 <= y < len(lines[x]):
    return lines[x][y]
  return None

count = 0
for x in range(len(lines)):
  for y in range(len(lines[x])):
    if safe_get(x, y) == "X" and safe_get(x + 1, y) == "M" and safe_get(x + 2, y) == "A" and safe_get(x + 3, y) == "S":
      count += 1
    if safe_get(x, y) == "X" and safe_get(x, y + 1) == "M" and safe_get(x, y + 2) == "A" and safe_get(x, y + 3) == "S":
      count += 1
    if safe_get(x, y) == "X" and safe_get(x - 1, y) == "M" and safe_get(x - 2, y) == "A" and safe_get(x - 3, y) == "S":
      count += 1
    if safe_get(x, y) == "X" and safe_get(x, y - 1) == "M" and safe_get(x, y - 2) == "A" and safe_get(x, y - 3) == "S":
      count += 1
    if safe_get(x, y) == "X" and safe_get(x + 1, y + 1) == "M" and safe_get(x + 2, y + 2) == "A" and safe_get(x + 3, y + 3) == "S":
      count += 1
    if safe_get(x, y) == "X" and safe_get(x - 1, y - 1) == "M" and safe_get(x - 2, y - 2) == "A" and safe_get(x - 3, y - 3) == "S":
      count += 1
    if safe_get(x, y) == "X" and safe_get(x + 1, y - 1) == "M" and safe_get(x + 2, y - 2) == "A" and safe_get(x + 3, y - 3) == "S":
      count += 1
    if safe_get(x, y) == "X" and safe_get(x - 1, y + 1) == "M" and safe_get(x - 2, y + 2) == "A" and safe_get(x - 3, y + 3) == "S":
      count += 1

print(count)