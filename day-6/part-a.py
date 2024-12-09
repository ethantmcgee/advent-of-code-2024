with open("input.txt") as file:
  lines = [[y for y in x.strip()] for x in file.readlines()]

x, y = -1, -1
dir = 0
for i in range(len(lines)):
  for j in range(len(lines[i])):
    if lines[i][j] == "^":
      x, y = i, j

def safe_get(x, y):
  if 0 <= x < len(lines) and 0 <= y < len(lines[x]):
    return lines[x][y]
  return None

while safe_get(x, y) != None:
  if dir == 0 and safe_get(x - 1, y) == "#":
    dir = (dir + 1) % 4
  elif dir == 1 and safe_get(x, y + 1) == "#":
    dir = (dir + 1) % 4
  elif dir == 2 and safe_get(x + 1, y) == "#":
    dir = (dir + 1) % 4
  elif dir == 3 and safe_get(x, y - 1) == "#":
    dir = (dir + 1) % 4
  elif dir == 0:
    lines[x][y] = "X"
    x -= 1
  elif dir == 1:
    lines[x][y] = "X"
    y += 1
  elif dir == 2:
    lines[x][y] = "X"
    x += 1
  elif dir == 3:
    lines[x][y] = "X"
    y -= 1

count = 0
for i in range(len(lines)):
  for j in range(len(lines[i])):
    if lines[i][j] == "X":
      count += 1

print(count)