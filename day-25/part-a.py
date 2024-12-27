with open("input.txt") as file:
  lines = [x.strip() for x in file.readlines()]

locks, keys = [], []

is_lock = False
current = []
for line in lines:
  if len(current) == 0:
    is_lock = line[0] == '#'
  if line == "":
    if is_lock:
      locks.append(current)
    else:
      keys.append(current)
    current = []
  else:
    current.append(line)
if is_lock:
  locks.append(current)
else:
  keys.append(current)

lock_profiles, key_profiles = [], []
for lock in locks:
  profile = []
  for i in range(len(lock[0])):
    profile.append([x[i] for x in lock].count('#') - 1)
  lock_profiles.append(profile)
for key in keys:
  profile = []
  for i in range(len(key[0])):
    profile.append([x[i] for x in key].count('#') - 1)
  key_profiles.append(profile)

possible = 0
for lock in lock_profiles:
  for key in key_profiles:
    good = True
    for i in range(len(lock)):
      if lock[i] + key[i] > 5:
        good = False
    if good:
      possible += 1
print(possible)
