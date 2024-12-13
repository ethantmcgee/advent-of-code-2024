import re

with open("input.txt") as file:
  lines = [x.strip() for x in file.readlines()]

A_COST = 3
B_COST = 1

def solve(button_a, button_b, prize):
  x_equation = (button_a[0], button_b[0], prize[0])
  y_equation = (button_a[1], button_b[1], prize[1])
  scaled_x_equation = (x_equation[0] * y_equation[0],
                       x_equation[1] * y_equation[0],
                       x_equation[2] * y_equation[0])
  scaled_y_equation = (y_equation[0] * x_equation[0],
                       y_equation[1] * x_equation[0],
                       y_equation[2] * x_equation[0])
  difference = (scaled_x_equation[1] - scaled_y_equation[1],
                scaled_x_equation[2] - scaled_y_equation[2])
  b, r = divmod(difference[1], difference[0])
  if r != 0:
      return None
  if x_equation[1] == 0:
      a, r = divmod((y_equation[2] - y_equation[1] * b), y_equation[0])
  else:
      a,r  = divmod((x_equation[2] - x_equation[1] * b), x_equation[0])
  if r == 0 and a >= 0 and b >= 0:
      return a, b
  return None

tokens = 0
a_button = (-1, -1)
b_button = (-1, -1)
prize = (-1, -1)
for i in range(len(lines)):
  if i % 4 == 0:
    parts = re.match(r"^Button A: X\+(\d+), Y\+(\d+)$", lines[i])
    a_button = (int(parts.group(1)), int(parts.group(2)))
  if i % 4 == 1:
    parts = re.match(r"Button B: X\+(\d+), Y\+(\d+)", lines[i])
    b_button = (int(parts.group(1)), int(parts.group(2)))
  if i % 4 == 2:
    parts = re.match(r"Prize: X=(\d+), Y=(\d+)", lines[i])
    prize = (int(parts.group(1)), int(parts.group(2)))
    # solve
    sol = solve(a_button, b_button, prize)
    if sol is not None:
      tokens += sol[0] * A_COST + sol[1] * B_COST

print(tokens)

