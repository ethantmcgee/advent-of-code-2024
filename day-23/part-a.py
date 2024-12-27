from collections import defaultdict
from itertools import combinations

with open("input.txt") as file:
  connections = [(x[0], x[1]) for x in [x.strip().split("-") for x in file.readlines()]]

graph = defaultdict(list)
for a, b in connections:
  graph[a].append(b)
  graph[b].append(a)

groups = set()
for computer, connected in graph.items():
  if computer[0] != 't':
    continue
  for c1, c2 in combinations(connected, 2):
    if c1 in graph[c2]:
      groups.add(tuple(sorted([computer, c1, c2])))

print(len(groups))
  