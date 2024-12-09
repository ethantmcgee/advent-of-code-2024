import re

with open("input.txt") as file:
  line = file.read()

sum = 0
for match in re.findall("mul\((\d{1,3}),(\d{1,3})\)", line):
  sum += int(match[0]) * int(match[1])

print(sum)