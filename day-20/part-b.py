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

  def circle_points(self, radius):
    s = set()
    for i in range(radius + 1):
        x, y = (i, radius - i)
        s.update([(x, y), (-x, -y), (x, -y), (-x, y)])
    result = []
    for d in s:
        result.append(tuple(x + y for x, y in zip((self.x, self.y), d)))
    return result
  
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
  best_path = []
  heappush(q, (0, start, [start]))
  while q:
    score, loc, path = heappop(q)
    if score > minimum:
      break
    if loc in visited and visited[loc] < score:
      continue
    visited[loc] = score
    if loc == end:
      minimum = score
      best_path = path
    # try turning
    for turn in [N, E, S, W]:
      new_point = loc.add(turn)
      if safe_get(new_point.x, new_point.y) is not None and safe_get(new_point.x, new_point.y) != "#":
        heappush(q, (score + 1, new_point, path + [new_point]))
  return (minimum, best_path)

saves = defaultdict(int)
original_min, original_path = solve()
for i in range(len(original_path)):
  for steps in range(2, 21):
    for j in original_path[i].circle_points(steps):
      try:
        idx = original_path.index(Point(j[0], j[1]))
        if idx - i - steps >= 100:
          saves[idx - i - steps] += 1
      except ValueError:
        pass

print(sum(saves.values()))