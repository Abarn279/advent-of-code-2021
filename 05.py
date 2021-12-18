from aoc_utils import Vector2, Grid2d

with open('./inp/05.txt') as f:
    lines = [line.rstrip() for line in f.readlines()]

# Part A and B
grid = Grid2d(0)
for line in lines:
    # string parsing into v2's for start/end
    starts, ends = line.split(' -> ')
    start = Vector2(*map(int,starts.split(',')))
    end = Vector2(*map(int,ends.split(',')))

    # UNCOMMENT FOR PART A
    # if not (start.x == end.x or start.y == end.y): continue

    # get direction of this line
    direction = (end - start).normalized().rounded()

    # lerp towards end
    while start != end:
        grid[start] += 1
        start = start + direction
    
    # add end
    grid[end] += 1

print(len([i for i in grid.values() if i > 1]))