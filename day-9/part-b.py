with open("input.txt") as file:
  descr = file.read().strip()

file_blocks = []
free_blocks = []
harddisk = []
id = 0
is_file = True
for x in descr:
  if is_file:
    file_blocks.append([len(harddisk), int(x), id])
    harddisk += [id] * int(x)
    id += 1
  else:
    free_blocks.append([len(harddisk), int(x)])
    harddisk += ["."] * int(x)
  is_file = not is_file

for file_block in file_blocks[::-1]:
  for free_block in free_blocks:
    if free_block[0] < file_block[0] and file_block[1] <= free_block[1]:
      # this block is big enough
      file_block[0] = free_block[0]
      free_block[1] -= file_block[1]
      free_block[0] += file_block[1]

chksum = 0
for file_block in file_blocks[::-1]:
  start = file_block[0]
  for i in range(file_block[1]):
    chksum += (start + i) * file_block[2]
print(chksum)
