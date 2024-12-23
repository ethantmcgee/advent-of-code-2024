from collections import defaultdict

with open("input.txt") as file:
  starts = [int(x.strip()) for x in file.readlines()]

bananas = defaultdict(int)

result = 0
for i in starts:
  my_counts = defaultdict(int)
  diffs = []
  secret = i
  last = secret % 10
  for j in range(2000):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    new_last = secret % 10
    diff = new_last - last
    diffs.append(diff)
    if len(diffs) == 4:
      if tuple(diffs) not in my_counts:
        my_counts[tuple(diffs)] += new_last
      diffs.pop(0)
    last = new_last
  for k, v in my_counts.items():
    bananas[k] += v  

print(max(bananas.values()))