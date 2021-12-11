from aoc_utils import Vector2
from searches import bfs

with open('./inp/09.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

# all directions
directions = [Vector2(0, 1), Vector2(0, -1), Vector2(1, 0), Vector2(-1, 0)]

# set up grid
grid = {}
for y in range(len(inp)):
    for x in range(len(inp[y])):
        grid[Vector2(x, y)] = int(inp[y][x])

# PART A
def is_low_point(grid, pos): 
    new_pos = [pos + d for d in directions if pos + d in grid]
    neighbors = [grid[v] for v in new_pos]
    return all(grid[pos] < n for n in neighbors)

# find summed risk sum
risk_sum = 0
for p in grid: 
    if is_low_point(grid, p):
        risk_sum += grid[p] + 1
print(risk_sum)

# Part B
def get_basin_size(lp):
    search_response = bfs(
        start = lp, 
        is_goal_fn = lambda n: False,
        get_neighbors_fn = lambda n: [n + d for d in directions if n + d in grid and grid[n + d] != 9],
        get_key_fn = lambda n: n
    )
    return len(search_response.visited)

low_points = [p for p in grid if is_low_point(grid, p)]
sizes = list(sorted([get_basin_size(lp) for lp in low_points], reverse=True))[:3]
print(sizes[0]*sizes[1]*sizes[2])