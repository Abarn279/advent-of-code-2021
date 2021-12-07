from collections import defaultdict

with open('./inp/06.txt') as f:
    fishies = list(map(int, f.read().split(',')))

num_fishies = defaultdict(lambda: 0)
for f in fishies: 
    num_fishies[f] += 1

for day in range(256):
    for t in range(9):
        num_fishies[t - 1] = num_fishies[t]

    num_fishies[8] = 0
    new = num_fishies[-1]
    num_fishies[6] += new
    num_fishies[8] += new
    num_fishies[-1] = 0

print(sum(num_fishies.values()))