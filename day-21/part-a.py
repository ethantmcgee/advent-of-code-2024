from functools import cache
from collections import defaultdict

# borrowed from advent of code subreddit, optimal paths from press to press
path = {}
path[('A', '<')] = 'v<<'
path[('A', '>')] = 'v'
path[('A', 'v')] = '<v'
path[('A', '^')] = '<'
path[('<', 'A')] = '>>^'
path[('<', '^')] = '>^'
path[('<', 'v')] = '>'
path[('>', 'A')] = '^'
path[('>', '^')] = '<^'
path[('>', 'v')] = '<'
path[('^', 'A')] = '>'
path[('^', '<')] = 'v<'
path[('^', '>')] = 'v>'
path[('v', 'A')] = '^>'
path[('v', '>')] = '>'
path[('v', '<')] = '<'

path[('A', '0')] = '<'
path[('A', '1')] = '^<<'
path[('A', '3')] = '^'
path[('A', '4')] = '^^<<'
path[('A', '5')] = '^^<' # or <^^
path[('A', '6')] = '^^'
path[('A', '7')] = '^^^<<'
path[('A', '9')] = '^^^'
path[('0', '2')] = '^'
path[('0', 'A')] = '>'
path[('1', '7')] = '^^'
path[('1', '9')] = '^^>>'
path[('2', '9')] = '^^>'
path[('3', '1')] = '<<'
path[('3', '4')] = '<<^' # or ^<<
path[('3', '5')] = '<^'
path[('3', '7')] = '<<^^'
path[('4', 'A')] = '>>vv'
path[('4', '5')] = '>'
path[('4', '8')] = '^>'
path[('4', '9')] = '^>>' # >>^
path[('5', 'A')] = 'vv>'
path[('5', '6')] = '>'
path[('5', '8')] = '^'
path[('6', 'A')] = 'vv'
path[('6', '4')] = '<<'
path[('6', '7')] = '^<<' # or <<^
path[('7', '0')] = '>vvv'
path[('7', '6')] = 'v>>'
path[('7', '6')] = 'v>>'
path[('7', '8')] = '>'
path[('7', '9')] = '>>'
path[('8', '0')] = 'vvv'
path[('8', '6')] = '>v' # or v>
path[('8', '9')] = '>'
path[('9', 'A')] = 'vvv'
path[('9', '3')] = 'vv'
path[('9', '6')] = 'v'
path[('9', '8')] = '<'
# end borrow

with open("input.txt") as file:
  codes = [x.strip() for x in file.readlines()]

@cache
def encode(code):
  type_code_moves = ''
  currently_pointing_at = 'A'
  for c in code:
    if c == currently_pointing_at: # we need to press the same button, no moves
      type_code_moves += 'A'
    else:
      type_code_moves += (path[(currently_pointing_at, c)] + 'A')
    currently_pointing_at = c
  return type_code_moves
  
def solve(depth):
  score = 0
  for code in codes:
    numeric_part = int(code[:-1]) # all but last last A
    type_code_moves = ''
    currently_pointing_at = 'A'
    for c in code:
      type_code_moves += (path[(currently_pointing_at, c)] + 'A')
      currently_pointing_at = c

    counts = defaultdict(int)
    parts = type_code_moves.split('A')
    for p in parts[:-1]:
        counts[p + 'A'] += 1

    for r in range(depth):
      new_counts = defaultdict(int)
      for k, v in counts.items():
          parts = encode(k).split('A')
          for p in parts[:-1]:
            new_counts[p + 'A'] += v
      counts = new_counts

    score += numeric_part * sum([len(k) * v for k, v in counts.items()])

  return score

print(solve(2))