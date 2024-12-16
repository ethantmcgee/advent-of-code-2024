from heapq import heappop, heappush
from math import inf

with open("input.txt") as file:
  grid = [[y for y in x.strip()] for x in file.readlines()]

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)

turns = {
  N: [E, W],
  E: [S, N],
  S: [W, E],
  W: [N, S],
}

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def add(self, dir):
    return Point(self.x + dir[0], self.y + dir[1])

  def __hash__(self):
    return hash((self.x, self.y))

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __str__(self):
    return f"({self.x}, {self.y})"

  def __repr__(self):
    return f"({self.x}, {self.y})"

  def __lt__(self, other):
    if self.x == other.x:
      return self.y < other.y
    return self.x < other.x

start = Point(-1, -1)
end = Point(-1, -1)
for x in range(len(grid)):
  for y in  range(len(grid[x])):
    if grid[x][y] == "S":
      start = Point(x, y)
    if grid[x][y] == "E":
      end = Point(x, y)

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

q = list()
visited = dict()
paths = list()

minimum = inf
heappush(q, (0, start, E, [start]))
while q:
  score, loc, dir, path = heappop(q)
  if score > minimum:
    break
  if (loc, dir) in visited and visited[(loc, dir)] < score:
    continue
  visited[(loc, dir)] = score
  if loc == end:
    minimum = score
    paths.append(path)
  # try going straight
  new_point = loc.add(dir)
  if safe_get(new_point.x, new_point.y) is not None and safe_get(new_point.x, new_point.y) != "#":
    heappush(q, (score + 1, new_point, dir, path + [new_point]))
  # try turning
  for turn in turns[dir]:
    new_point = loc.add(turn)
    if safe_get(new_point.x, new_point.y) is not None and safe_get(new_point.x, new_point.y) != "#":
      heappush(q, (score + 1001, new_point, turn, path + [new_point]))

set = set()
for path in paths:
  for point in path:
    set.add(point)

print(len(set))
