with open("input.txt") as file:
  lines = [[y for y in x.strip()] for x in file.readlines()]

def safe_get(x, y):
  if 0 <= x < len(lines) and 0 <= y < len(lines[x]):
    return lines[x][y]
  return None

def try_hike(x, y, cur):
  next = str(int(cur) + 1)
  if cur == "9" and safe_get(x, y) == "9":
    return {(x, y)}
  pos = set()
  if safe_get(x - 1, y) == next:
    pos = pos.union(try_hike(x - 1, y, next))
  if safe_get(x + 1, y) == next:
    pos = pos.union(try_hike(x + 1, y, next))
  if safe_get(x, y - 1) == next:
    pos = pos.union(try_hike(x, y - 1, next))
  if safe_get(x, y + 1) == next:
    pos = pos.union(try_hike(x, y + 1, next))
  return pos

reachable_ends = 0
for i in range(len(lines)):
  for j in range(len(lines[i])):
    if lines[i][j] == "0":
      ends = try_hike(i, j, "0")
      reachable_ends += len(ends)

print(reachable_ends)