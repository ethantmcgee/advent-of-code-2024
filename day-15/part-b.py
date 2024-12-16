with open("input.txt") as file:
  data = [x.strip() for x in file.readlines()]

middle = data.index("")

class Box:
  def __init__(self, point_a, point_b):
    self.point_a = point_a
    self.point_b = point_b

  def move(self, dir):
    self.point_a = (self.point_a[0] + dir[0], self.point_a[1] + dir[1])
    self.point_b = (self.point_b[0] + dir[0], self.point_b[1] + dir[1])

  def hit(self, loc):
    return self.point_a == loc or self.point_b == loc

  def get_a(self):
    return self.point_a

  def get_b(self):
    return self.point_b

# transform grid
boxes = []
old_grid = [[y for y in x.strip()] for x in data[:middle]]
new_grid = []
for line in old_grid:
  new_line = []
  for char in line:
    if char == '#':
      new_line.append("#")
      new_line.append("#")
    if char == 'O':
      new_line.append("[")
      new_line.append("]")
    if char == '.':
      new_line.append(".")
      new_line.append(".")
    if char == '@':
      new_line.append("@")
      new_line.append(".")
  new_grid.append(new_line)
grid = new_grid[:]

movement = "".join(data[middle + 1:])

robot = (-1, -1)
for x in range(len(grid)):
  for y in range(len(grid[x])):
    if grid[x][y] == "@":
      robot = (x, y)
      grid[x][y] = "."
    if grid[x][y] == "[":
      boxes.append(Box((x, y), (x, y + 1)))
      grid[x][y] = "."
      grid[x][y + 1] = "."

def safe_get(x, y):
  if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
    return grid[x][y]
  return None

def print_grid():
  for x in range(len(grid)):
    for y in range(len(grid[x])):
      if (x, y) == robot:
        print("@", end="")
      elif (x, y) in [z.get_a() for z in boxes]:
        print("[", end="")
      elif (x, y) in [z.get_b() for z in boxes]:
        print("]", end="")
      else:
        print(grid[x][y], end="")
    print()
  print()

def boxes_to_move(cur_box, loc, dir):
  to_move = {box for box in boxes if box.hit(loc) and box != cur_box}
  for box in to_move:
    to_move = to_move.union(boxes_to_move(box, (box.get_a()[0] + dir[0], box.get_a()[1] + dir[1]), dir))
    to_move = to_move.union(boxes_to_move(box, (box.get_b()[0] + dir[0], box.get_b()[1] + dir[1]), dir))
  return to_move

def boxes_safe_to_move(boxes, dir):
  for box in boxes:
    new_point_a = (box.get_a()[0] + dir[0], box.get_a()[1] + dir[1])
    if safe_get(new_point_a[0], new_point_a[1]) == "#":
      return False
    new_point_b = (box.get_b()[0] + dir[0], box.get_b()[1] + dir[1])
    if safe_get(new_point_b[0], new_point_b[1]) == "#":
      return False
  return True

def move_boxes(boxes, dir):
  for box in boxes:
    box.move(dir)

def push(loc, dir):
  new_dir = (loc[0] + dir[0], loc[1] + dir[1])
  my_boxes = boxes_to_move(None, new_dir, dir)
  if safe_get(new_dir[0], new_dir[1]) != "#" and boxes_safe_to_move(my_boxes, dir):
    move_boxes(my_boxes, dir)
    return new_dir
  else: # nope can't move
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
    if (x, y) in [z.get_a() for z in boxes]:
      score += 100 * x + y

print(score)