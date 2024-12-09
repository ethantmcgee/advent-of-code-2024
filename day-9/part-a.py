with open("input.txt") as file:
  descr = file.read().strip()

file_blocks = []
free_blocks = []
harddisk = []
id = 0
is_file = True
for x in descr:
  if is_file:
    file_blocks.append((len(harddisk), int(x)))
    harddisk += [id] * int(x)
    id += 1
  else:
    free_blocks.append((len(harddisk), int(x)))
    harddisk += ["."] * int(x)
  is_file = not is_file

file_pos = []
for x in file_blocks:
  start = x[0]
  for i in range(x[1]):
    file_pos.append(start + i)

chksum = 0
idx = 0
end = file_pos.pop()
while idx <= end:
  if harddisk[idx] != ".":
    chksum += harddisk[idx] * idx
  else:
    chksum += harddisk[end] * idx
    end = file_pos.pop()
  idx += 1

print(chksum)
  