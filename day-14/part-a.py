import re

with open("input.txt") as file:
  data = [x.strip() for x in file.readlines()]

WIDTH = 101
HEIGHT = 103
STEPS = 20000

robots = []
for robot in data:
  parts = re.match(r"p=(\-?\d+),(\-?\d+) v=(\-?\d+),(\-?\d+)", robot)
  robots.append([(int(parts.group(1)), int(parts.group(2))), (int(parts.group(3)), int(parts.group(4)))])

def print_maze():
  for y in range(HEIGHT):
    for x in range(WIDTH):
      ct = [z[0] for z in robots].count((x, y))
      print(ct if ct > 0 else ".", end="")
    print()
  print()

for i in range(STEPS):
  for robot in robots:
    x, y = robot[0]
    vx, vy = robot[1]
    x += vx
    y += vy
    if x < 0:
      x = WIDTH + x
    if x >= WIDTH:
      x = x - WIDTH
    if y < 0:
      y = HEIGHT + y
    if y >= HEIGHT:
      y = y - HEIGHT
    robot[0] = (x, y)
  print("Step", i)
  print_maze()

quad_1, quad_2, quad_3, quad_4 = 0, 0, 0, 0
for y in range(HEIGHT):
  for x in range(WIDTH):
    ct = [z[0] for z in robots].count((x, y))
    if ct > 0:
      if 0 <= x < WIDTH // 2 and 0 <= y < HEIGHT // 2:
        quad_1 += ct
      if 0 <= x < WIDTH // 2 and HEIGHT // 2 < y < HEIGHT:
        quad_2 += ct
      if WIDTH // 2 < x < WIDTH and 0 <= y < HEIGHT // 2:
        quad_3 += ct
      if WIDTH // 2 < x < WIDTH and HEIGHT // 2 < y < HEIGHT:
        quad_4 += ct

print(quad_1 * quad_2 * quad_3 * quad_4)