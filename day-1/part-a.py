list_a, list_b = [], []
with open('input.txt') as file:
  for line in file.readlines():
    a, b = map(int, [x for x in line.strip().split(' ') if len(x) > 0])
    list_a.append(a)
    list_b.append(b)

list_a = sorted(list_a)
list_b = sorted(list_b)

sum = 0
for i in range(len(list_a)):
  sum += abs(list_a[i] - list_b[i])

print(sum)