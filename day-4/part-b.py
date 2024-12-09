with open("demo.txt") as file:
  lines = [x.strip() for x in file.readlines()]

def safe_get(x, y):
  if 0 <= x < len(lines) and 0 <= y < len(lines[x]):
    return lines[x][y]
  return ""

count = 0
for x in range(len(lines)):
  for y in range(len(lines[x])):
    if safe_get(x - 1, y - 1) + safe_get(x, y) + safe_get(x + 1, y + 1) in ["MAS", "SAM"] and safe_get(x - 1, y + 1) + safe_get(x, y) + safe_get(x + 1, y - 1) in ["MAS", "SAM"]:
      count += 1

print(count)