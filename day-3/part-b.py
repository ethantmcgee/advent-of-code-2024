import re

with open("input.txt") as file:
  line = file.read()

enabled = True
sum = 0
for match in re.findall("mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)", line):
  if len(match[0]) > 0 and len(match[1]) > 0 and enabled:
    sum += int(match[0]) * int(match[1])
  elif len(match[2]) > 0:
    enabled = True
  elif len(match[3]) > 0:
    enabled = False

print(sum)