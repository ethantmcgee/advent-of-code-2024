from functools import cache

with open("input.txt") as file:
  data = [x.strip() for x in file.readlines()]

patterns = sorted([(len(x), x) for x in data[0].split(", ")])[::-1]

towels = data[2:]

@cache
def solve(towel):
  combinations = 0
  for pattern in patterns:
    if towel == pattern[1]:
      combinations += 1
    elif towel.startswith(pattern[1]):
      combinations += solve(towel[pattern[0]:])
  return combinations
  

possible = 0
for towel in towels:
  possible += (1 if solve(towel) > 0 else 0)

print(possible)