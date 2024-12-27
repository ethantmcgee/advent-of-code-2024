from collections import defaultdict
from itertools import combinations

with open("input.txt") as file:
  connections = [(x[0], x[1]) for x in [x.strip().split("-") for x in file.readlines()]]

graph = defaultdict(list)
for a, b in connections:
  graph[a].append(b)
  graph[b].append(a)

def spider_consume(nodes):
  for possible in graph.keys():
    if possible in nodes:
      continue
    all = True
    for node in nodes:
      if possible not in graph[node]:
        all = False
    if all:
      nodes.add(possible)
  return nodes

best = []
for computer, connected in graph.items():
  if computer[0] != 't' or computer in best:
    continue
  for c1, c2 in combinations(connected, 2):
    if c2 in graph[c1]:
      # we found a tuple with a t, now spider as much as possible
      consumed = spider_consume({computer, c1, c2})
      if len(consumed) > len(best):
        best = consumed

print(",".join(sorted(best)))
