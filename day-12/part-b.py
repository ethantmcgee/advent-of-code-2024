with open("demo.txt") as file:
  grid = [[y for y in x.strip()] for x in file.readlines()]

def safe_get(x, y):
  if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
    return grid[x][y]
  return None

def flood(x, y, char):
  grid[x][y] = '.' # we've been here don't come here again
  island_parts = {(x, y)}
  if safe_get(x - 1, y) == char:
    island_parts = island_parts.union(flood(x - 1, y, char))
  if safe_get(x + 1, y) == char:
    island_parts = island_parts.union(flood(x + 1, y, char))
  if safe_get(x, y - 1) == char:
    island_parts = island_parts.union(flood(x, y - 1, char))
  if safe_get(x, y + 1) == char:
    island_parts = island_parts.union(flood(x, y + 1, char))
  return island_parts

def get_area_permieter_side_count(island):
  # perimeter counting
  perimeter_counts = 0
  for land in island:
    if (land[0] - 1, land[1]) not in island:
      perimeter_counts += 1
    if (land[0] + 1, land[1]) not in island:
      perimeter_counts += 1
    if (land[0], land[1] - 1) not in island:
      perimeter_counts += 1
    if (land[0], land[1] + 1) not in island:
      perimeter_counts += 1
  # corner counting (# of corners = # of sides)
  corner_count = 0
  for land in island:
      N = (land[0], land[1] - 1) in island
      E = (land[0] + 1, land[1]) in island
      S = (land[0], land[1] + 1) in island
      W = (land[0] - 1, land[1]) in island
      NE = (land[0] + 1, land[1] - 1) in island
      SE = (land[0] + 1, land[1] + 1) in island
      NW = (land[0] - 1, land[1] - 1) in island
      SW = (land[0] - 1, land[1] + 1) in island
      # A tile may qualify as a corner in multiple ways
      # single nodes (no adjacent)
      if(not N and not E and not S and not W):
        corner_count += 4
      # pokey nodes (touches zone on just 1 side)
      if(N and not E and not S and not W): 
        corner_count += 2
      if(E and not S and not W and not N):
        corner_count += 2
      if(S and not W and not N and not E):
        corner_count += 2
      if(W and not N and not E and not S):
        corner_count += 2
      # convex corners
      if(S and E and not N and not W):
        corner_count += 1
      if(S and W and not N and not E):
        corner_count += 1
      if(N and E and not S and not W):
        corner_count += 1
      if(N and W and not S and not E):
        corner_count += 1
      # concave corners
      if(E and N and not NE):
        corner_count += 1
      if(E and S and not SE):
        corner_count += 1
      if(W and N and not NW):
        corner_count += 1
      if(W and S and not SW):
        corner_count += 1
  return (len(island), perimeter_counts, corner_count)

sum = 0
for x in range(len(grid)):
  for y in range(len(grid[x])):
    if grid[x][y] != ".":
      island = flood(x, y, grid[x][y])
      counts = get_area_permieter_side_count(island)
      sum += counts[0] * counts[2]

print(sum)