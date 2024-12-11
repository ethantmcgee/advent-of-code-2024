from collections import defaultdict
from json import dumps

with open("input.txt") as file:
  stones = [x for x in map(int, file.read().strip().split(" "))]

stones_freq = defaultdict(int)
for stone in stones:
  stones_freq[stone] += 1


def blink(stones_freq):
  new_stones_freq = defaultdict(int)
  for stone in stones_freq:
    if stone == 0:
      new_stones_freq[1] += stones_freq[stone]
    elif len(str(stone)) % 2 == 0:
      dist = len(str(stone)) // 2
      new_stones_freq[int(str(stone)[:dist])] += stones_freq[stone]
      new_stones_freq[int(str(stone)[dist:])] += stones_freq[stone]
    else:
      new_stones_freq[stone * 2024] += stones_freq[stone]
  return new_stones_freq
    

for i in range(25):
  stones_freq = blink(stones_freq)

sum = 0
for stone, count in stones_freq.items():
  sum += count

print(sum)
  