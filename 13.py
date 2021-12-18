from aoc_utils import Vector2
import numpy
import re

with open('./inp/13.txt') as f:
    coords, folds = f.read().split('\n\n')
    coords = [Vector2(*map(int, i.split(','))) for i in coords.split('\n')]
    folds = folds.split('\n')

def flip_up(grid, line):
    overlay_grid = numpy.flipud(grid[line + 1:])
    original_grid = grid[:line]

    # this is the top grid that's unchanged becuase the fold doesn't reach it
    top_grid = original_grid[:len(original_grid) - len(overlay_grid)]

    # this is the grid that is actually impacted by the overlay
    to_overlay_on_grid = original_grid[len(original_grid) - len(overlay_grid):]

    # complete the overlay
    completed_overlay = numpy.where(overlay_grid == '#', overlay_grid, to_overlay_on_grid)

    if top_grid:
        final = numpy.row_stack((top_grid, completed_overlay))
    else: final = completed_overlay
    
    return final.tolist()
    

def flip_left(grid, line):
    grid = numpy.array(grid)
    original_grid = grid[:, :line]
    overlay_grid = numpy.fliplr(grid[:, line+1:])
    
    # this is the left grid that's unchanged becuase the fold doesn't reach it
    left_grid = original_grid[:, :len(original_grid[0]) - len(overlay_grid[0])]
    
    # this is the grid that is actually impacted by the overlay
    to_overlay_on_grid = original_grid[:, len(original_grid[0]) - len(overlay_grid[0]):]

    # complete the overlay
    completed_overlay = numpy.where(overlay_grid == '#', overlay_grid, to_overlay_on_grid)

    if (left_grid.tolist()):
        final = numpy.column_stack((left_grid, completed_overlay))
    else: final = completed_overlay

    return final.tolist()

# Set up grid
maxx = max(coords, key=lambda c: c.x).x
maxy = max(coords, key=lambda c: c.y).y

grid = [['.' for x in range(maxx + 1)] for y in range(maxy + 1)]

for c in coords:
    grid[c.y][c.x] = '#'

# Part A and B
count = 0
for f in folds:
    # if count == 1:            # UNCOMMENT FOR PART A
    #     print( numpy.count_nonzero(numpy.array(grid) == '#') )
    #     break

    [axis, line] = re.match(r'fold along (\w)=(\d+)', f).groups()
    if axis == 'y': grid = flip_up(grid, int(line))
    elif axis == 'x': grid = flip_left(grid, int(line))

    count += 1

for y in grid:
    for x in y:
        print(x, end='')
    print('\n')
