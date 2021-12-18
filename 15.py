from aoc_utils import Grid2d, Vector2
from searches import astar

with open('./inp/15.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]
    for i in range(len(inp)):
        inp[i] = list(map(int, list(inp[i])))
    grid = Grid2d(None, inp)

goal = Vector2(len(inp[0]) - 1, len(inp) - 1)

def is_goal_fn(n):
    return n[0] == goal

def heuristic_fn(n):
    return n[0].manhattan_distance(goal)

def cost_fn(n, m):
    return grid[m[0]]

def get_neighbors_fn(n):
    # ignore places already been
    neighbors = [(i, n[1].copy()) for i in grid.get_cardinal_neighbors(n[0]) if i not in n[1]] 

    for neighbor in neighbors:
        neighbor[1].add(neighbor[0])

    return neighbors
    
# A* node is - 
# 0. most recent position
# 1. set of all positions entered

# Part A
res = astar(
    start = (Vector2(0, 0), set([Vector2(0, 0)])),
    is_goal_fn = is_goal_fn,
    heuristic_fn = heuristic_fn,
    cost_fn = cost_fn,
    get_neighbors_fn = get_neighbors_fn,
    get_key_fn = lambda n: str(n[0])
)

print(res.cost)

# Part B
goal = Vector2(len(inp[0]), len(inp)) * Vector2(5, 5) - Vector2(1, 1)

def get_risk(p): 
    grid_right = p.x // len(inp)
    grid_down = p.y // len(inp)
    times_add = grid_right + grid_down
    real = grid[Vector2(p.x % len(inp), p.y % len(inp))]

    # yicky way to wrap from 9 to 1 cause i'm not smart
    edited = (real + times_add) % 9
    return edited if edited != 0 else 9


def get_neighbors_fn(n):
    # ignore places already been
    neighbors = [(i, n[1].copy()) for i in [n[0] + d for d in [Vector2(0, 1), Vector2(1, 0), Vector2(-1, 0), Vector2(0, -1)] if (n[0] + d).x >= 0 and (n[0] + d).y >= 0 and (n[0] + d).x <= goal.x and (n[0] + d).y <= goal.y] if i not in n[1]] 

    for neighbor in neighbors:
        neighbor[1].add(neighbor[0])

    return neighbors

def cost_fn(n, m):
    return get_risk(m[0])

res = astar(
    start = (Vector2(0, 0), set([Vector2(0, 0)])),
    is_goal_fn = is_goal_fn,
    heuristic_fn = heuristic_fn,
    cost_fn = cost_fn,
    get_neighbors_fn = get_neighbors_fn,
    get_key_fn = lambda n: str(n[0])
)

print(res.cost)