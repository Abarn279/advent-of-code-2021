from searches import bfs
from collections import defaultdict

with open('./inp/12.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

connections = defaultdict(lambda: set())

for i in inp:
    frm, to = i.split('-')
    connections[frm].add(to)
    connections[to].add(frm)

# Part A
def get_neighbors_fn(n): 
    path = n.split(',')
    neighbors = []

    for c in connections[path[-1]]:

        # skip if minor cave
        if c.islower() and c in path:
            continue

        neighbors.append(",".join(path) + f',{c}')
    
    return neighbors

def is_goal_fn(n): 
    x = n.split(',')[-1]
    return x == 'end'

response = bfs(start='start',
    is_goal_fn=is_goal_fn,
    get_neighbors_fn=get_neighbors_fn,
    get_key_fn = lambda n: n,
    find_all_goals=True
)

print(len(response.all_final_nodes))

# Part B
def get_neighbors_fn(n): 
    path = n.split(',')
    neighbors = []

    times_visited = {c: path.count(c) for c in path if c not in ['start', 'end'] and c.islower()}

    for c in connections[path[-1]]:

        if c == 'start': continue

        if c.islower() and c != 'end' and any(True for i in times_visited if times_visited[i] > 1 and c in path):
            continue

        neighbors.append(",".join(path) + f',{c}')
    
    return neighbors

response = bfs(start='start',
    is_goal_fn=is_goal_fn,
    get_neighbors_fn=get_neighbors_fn,
    get_key_fn = lambda n: n,
    find_all_goals=True
)

print(len(response.all_final_nodes))