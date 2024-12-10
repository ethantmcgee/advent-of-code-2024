with open("input.txt") as file:
  lines = [[y for y in x.strip()] for x in file.readlines()]

def safe_get(x, y):
  if 0 <= x < len(lines) and 0 <= y < len(lines[x]):
    return lines[x][y]
  return None

def try_hike(x, y, cur):
  next = str(int(cur) + 1)
  if cur == "9" and safe_get(x, y) == "9":
    return 1
  sum = 0
  if safe_get(x - 1, y) == next:
    sum += try_hike(x - 1, y, next)
  if safe_get(x + 1, y) == next:
    sum += try_hike(x + 1, y, next)
  if safe_get(x, y - 1) == next:
    sum += try_hike(x, y - 1, next)
  if safe_get(x, y + 1) == next:
    sum += try_hike(x, y + 1, next)
  return sum

reachable_ends = 0
for i in range(len(lines)):
  for j in range(len(lines[i])):
    if lines[i][j] == "0":
      reachable_ends += try_hike(i, j, "0")

print(reachable_ends)