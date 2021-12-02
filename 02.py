from aoc_utils import Vector2, Vector3

with open('./inp/02.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]


# Part A
pos = Vector2(0, 0) # x is horizontal, y is depth

for cmd in inp:
    d, n = cmd.split(' ')
    if d == 'forward': pos.x += int(n)
    if d == 'down': pos.y += int(n)
    if d == 'up': pos.y -= int(n)

print(pos.x * pos.y)

# Part B
pos = Vector3(0, 0, 0) # x is horizontal, y is depth, z is current aim

for cmd in inp: 
    d, n = cmd.split(' ')
    if d == 'forward': 
        pos.x += int(n)
        pos.y += pos.z * int(n)
    if d == 'down': pos.z += int(n)
    if d == 'up': pos.z -= int(n)

print(pos.x * pos.y)