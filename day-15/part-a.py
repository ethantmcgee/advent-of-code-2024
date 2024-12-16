with open("input.txt") as file:
  data = [x.strip() for x in file.readlines()]

middle = data.index("")

grid = lines = [[y for y in x.strip()] for x in data[:middle]]

movement = "".join(data[middle + 1:])

robot = (-1, -1)
for x in range(len(grid)):
  for y in range(len(grid[x])):
    if grid[x][y] == "@":
      robot = (x, y)

def safe_get(x, y):
  if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
    return grid[x][y]
  return None

def print_grid():
  for x in range(len(grid)):
    for y in range(len(grid[x])):
      print(grid[x][y], end="")
    print()
  print()

def push(loc, dir):
  me = safe_get(loc[0], loc[1])
  next = safe_get(loc[0] + dir[0], loc[1] + dir[1])
  if next == "O":
    push((loc[0] + dir[0], loc[1] + dir[1]), dir)
    next = safe_get(loc[0] + dir[0], loc[1] + dir[1])
  if next == ".":
    grid[loc[0]][loc[1]] = next
    grid[loc[0] + dir[0]][loc[1] + dir[1]] = me
    return (loc[0] + dir[0], loc[1] + dir[1])
  return loc

for move in movement:
  if move == "^":
    robot = push(robot, (-1, 0))
  elif move == ">":
    robot = push(robot, (0, 1))
  elif move == "v":
    robot = push(robot, (1, 0))
  elif move == "<":
    robot = push(robot, (0, -1))

score = 0
for x in range(len(grid)):
  for y in range(len(grid[x])):
    if grid[x][y] == "O":
      score += 100 * x + y

print(score)