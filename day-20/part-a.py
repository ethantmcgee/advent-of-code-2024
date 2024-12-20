from heapq import heappop, heappush
from math import inf
from collections import defaultdict

with open("input.txt") as file:
  grid = [[y for y in x.strip()] for x in file.readlines()]

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)

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

def solve():
  q = list()
  visited = dict()
  minimum = inf
  heappush(q, (0, start))
  while q:
    score, loc = heappop(q)
    if score > minimum:
      break
    if loc in visited and visited[loc] < score:
      continue
    visited[loc] = score
    if loc == end:
      minimum = score
    # try turning
    for turn in [N, E, S, W]:
      new_point = loc.add(turn)
      if safe_get(new_point.x, new_point.y) is not None and safe_get(new_point.x, new_point.y) != "#":
        heappush(q, (score + 1, new_point))
  return minimum

saves = defaultdict(int)
original_min = solve()
for x in range(1, len(grid) - 1):
  for y in  range(1, len(grid[x]) - 1):
    if grid[x][y] == "#": # change this to a '.' and try again to see if we save time
      grid[x][y] = "."
      new_min = solve()
      if 100 <= (original_min - new_min):
        saves[(original_min - new_min)] += 1
      grid[x][y] = "#"

print(saves)
print(sum(saves.values()))