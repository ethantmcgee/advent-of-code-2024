from collections import defaultdict

with open("input.txt") as file:
  lines = [[y for y in x.strip()] for x in file.readlines()]

radios = defaultdict(list)

for x in range(len(lines)):
  for y in range(len(lines[x])):
    if lines[x][y] != ".":
      radios[lines[x][y]].append((x, y))

antinodes = []
for type, rs in radios.items():
  for a, b in [(a, b) for a in rs for b in rs if a != b]:
    dx=a[0] - b[0]
    dy=a[1] - b[1]

    nx=b[0]
    ny=b[1]

    while 0 <= nx < len(lines) and 0 <= ny < len(lines[nx]):
      if (nx, ny) not in antinodes:
        antinodes.append((nx, ny))
      nx -= dx
      ny -= dy

print(len(antinodes))