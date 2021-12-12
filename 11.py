from aoc_utils import Vector2, Grid2d

with open('./inp/11.txt') as f:
    octos = [list(map(int, line.rstrip())) for line in f.readlines()]

DIRECTIONS = [Vector2.create(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if x != 0 or y != 0]

grid = Grid2d(None, octos)

total_flashes = 0
for step in range(1000):

    to_flash = set()
    has_flashed = set()

    # Increment all energy levels
    for k in grid.keys():
        grid[k] += 1
        if grid[k] > 9:
            to_flash.add(k)

    # Flash until everyone's done
    while to_flash:
        c = to_flash.pop()
        has_flashed.add(c)

        # Increment all neighbors
        for d in DIRECTIONS:
            if c + d in grid: 
                grid[c + d] += 1
                if grid[c + d] > 9 and c + d not in has_flashed:
                    to_flash.add(c + d)
        
    for k in has_flashed:
        grid[k] = 0

    total_flashes += len(has_flashed)

    # PART A 
    if step == 99:
        print("total flashes: " + str(total_flashes))

    # PART B
    if len(has_flashed) == len(grid.keys()):
        print("sync step: " + str(step + 1))
        break
