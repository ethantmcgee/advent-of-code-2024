with open("input.txt") as file:
  lines = [[y for y in x.strip()] for x in file.readlines()]

start_x, start_y = -1, -1
dir = 0
for i in range(len(lines)):
  for j in range(len(lines[i])):
    if lines[i][j] == "^":
      start_x, start_y = i, j

def safe_get(x, y):
  if 0 <= x < len(lines) and 0 <= y < len(lines[x]):
    return lines[x][y]
  return None

def simulate(x, y, dir, path):
  while safe_get(x, y) != None:
    if (x, y, dir) in path:
      return 1
    if dir == 0 and safe_get(x - 1, y) == "#":
      dir = (dir + 1) % 4
    elif dir == 1 and safe_get(x, y + 1) == "#":
      dir = (dir + 1) % 4
    elif dir == 2 and safe_get(x + 1, y) == "#":
      dir = (dir + 1) % 4
    elif dir == 3 and safe_get(x, y - 1) == "#":
      dir = (dir + 1) % 4
    elif dir == 0:
      path.append((x, y, dir))
      lines[x][y] = "X"
      x -= 1
    elif dir == 1:
      path.append((x, y, dir))
      lines[x][y] = "X"
      y += 1
    elif dir == 2:
      path.append((x, y, dir))
      lines[x][y] = "X"
      x += 1
    elif dir == 3:
      path.append((x, y, dir))
      lines[x][y] = "X"
      y -= 1
  return 0

x, y = start_x, start_y
path = []
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
    path.append((x, y, dir))
    lines[x][y] = "X"
    x -= 1
  elif dir == 1:
    path.append((x, y, dir))
    lines[x][y] = "X"
    y += 1
  elif dir == 2:
    path.append((x, y, dir))
    lines[x][y] = "X"
    x += 1
  elif dir == 3:
    path.append((x, y, dir))
    lines[x][y] = "X"
    y -= 1

blocks = []
for pos in path[1:]:
  orig = lines[pos[0]][pos[1]]
  lines[pos[0]][pos[1]] = "#"
  res = simulate(start_x, start_y, 0, [])
  if res > 0 and (pos[0], pos[1]) not in blocks:
    blocks.append((pos[0], pos[1]))
  lines[pos[0]][pos[1]] = orig
  
print(len(blocks))