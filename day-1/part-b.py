list_a, list_b = [], []
with open('input.txt') as file:
  for line in file.readlines():
    a, b = map(int, [x for x in line.strip().split(' ') if len(x) > 0])
    list_a.append(a)
    list_b.append(b)

sum = 0
for i in range(len(list_a)):
  sum += list_a[i] * list_b.count(list_a[i])

print(sum)