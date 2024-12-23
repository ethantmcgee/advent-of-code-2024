with open("input.txt") as file:
  starts = [int(x.strip()) for x in file.readlines()]

result = 0
for i in starts:
  secret = i
  for j in range(2000):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
  result += secret
print(result)