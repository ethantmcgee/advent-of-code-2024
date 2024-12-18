from math import inf

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)

with open("input.txt", "r") as file:
  coords = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in file.readlines()]

EXIT = 70
STEPS = 1024

start = (0, 0)
end = (EXIT, EXIT)

def in_world(x, y):
  return 0 <= x <= EXIT and 0 <= y <= EXIT

def is_corrupted(x, y):
  return (x, y) in coords[:STEPS]

visited = list()
queue = [(0, start, [start])]
minimum = inf
while len(queue) > 0:
  new_queue = []

  for score, loc, path in queue:
    if loc in visited:
      continue
    
    visited.append(loc)

    if loc == end:
      minimum = score
    # try north
    new_point = (loc[0] + N[0], loc[1] + N[1])
    if in_world(new_point[0], new_point[1]) and not is_corrupted(new_point[0], new_point[1]) and new_point not in visited:
      new_queue.append((score + 1, new_point, path + [new_point]))
    # try east
    new_point = (loc[0] + E[0], loc[1] + E[1])
    if in_world(new_point[0], new_point[1]) and not is_corrupted(new_point[0], new_point[1]) and new_point not in visited:
      new_queue.append((score + 1, new_point, path + [new_point]))
    # try south
    new_point = (loc[0] + S[0], loc[1] + S[1])
    if in_world(new_point[0], new_point[1]) and not is_corrupted(new_point[0], new_point[1]) and new_point not in visited:
      new_queue.append((score + 1, new_point, path + [new_point]))
    # try west
    new_point = (loc[0] + W[0], loc[1] + W[1])
    if in_world(new_point[0], new_point[1]) and not is_corrupted(new_point[0], new_point[1]) and new_point not in visited:
      new_queue.append((score + 1, new_point, path + [new_point]))

  queue = new_queue

print(minimum)
