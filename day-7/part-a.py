with open("input.txt") as file:
  lines = [x.strip() for x in file.readlines()]

def try_combine(a, b, rest, ans):
  if len(rest) == 0:
    return a + b == ans or a * b == ans
  return try_combine(a + b, rest[0], rest[1:], ans) or try_combine(a * b, rest[0], rest[1:], ans)

sum = 0
for line in lines:
  ans, rest = line.split(": ")
  ops = rest.split(" ")
  ans = int(ans)
  ops = [x for x in map(int, ops)]
  
  if try_combine(ops[0], ops[1], ops[2:], ans):
    sum += ans

print(sum)
    

  