MIN_INCREASE = 1
MAX_INCREASE = 3
TOLERATIONS = 1

def is_safe(diffs):
  wants_positive = diffs[0] > 0
  
  all_same = False
  all_safe = False
  if wants_positive:
    all_same = all(x >= 0 for x in diffs)
    all_safe = all(MIN_INCREASE <= x <= MAX_INCREASE for x in diffs)
  else:
    all_same = all(x <= 0 for x in diffs)
    all_safe = all(-MIN_INCREASE >= x >= -MAX_INCREASE for x in diffs)

  return all_same and all_safe

safe_levels = 0
with open("input.txt") as file:
  lines = file.readlines()
  for line in lines:
    levels = [y for y in map(int, [x for x in line.strip().split(" ") if len(x) > 0])]
    diffs = [x - y for x, y in zip(levels, levels[1:])]
    
    if is_safe(diffs):
      safe_levels += 1
    else:
      # try removing one entry from levels then check safety
      for i in range(len(levels)):
        new_levels = levels[:]
        new_levels.pop(i)
        new_diffs = [x - y for x, y in zip(new_levels, new_levels[1:])]
        if is_safe(new_diffs):
          safe_levels += 1
          break

print(safe_levels)