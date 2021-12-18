from collections import Counter, defaultdict

with open('./inp/14.txt') as f:
    ptemplate = f.readline()[:-1];f.readline()
    prules = [line.rstrip() for line in f.readlines()]
    prules = {i.split(' -> ')[0]: i.split(' -> ')[1] for i in prules}

# Part A, naive solution 
for step in range(40):
    final = ''
    for ci in range(len(ptemplate) - 1):
        final = final + ptemplate[ci]
        pair = ptemplate[ci] + ptemplate[ci + 1]
        if pair in prules:
            final = final + prules[pair]
    final = final + ptemplate[-1]
    ptemplate = final

res = Counter(ptemplate)
print(ptemplate.count(max(res, key=res.get)) - ptemplate.count(min(res, key=res.get)))

# Part B, non-naive solution. keeping track of the count of pairs, don't care about order, as well as keeping track of a count of added chars
pairs_count = {ptemplate[i] + ptemplate[i+1]: ptemplate.count(ptemplate[i] + ptemplate[i+1]) for i in range(len(ptemplate) - 1)}
char_count = defaultdict(lambda: 0)
char_count.update({i: ptemplate.count(i) for i in ptemplate})

for step in range(40):    
    new_pairs_count = defaultdict(lambda: 0)
    for r in list(pairs_count.keys()):
        new = r[0] + prules[r] + r[1]
        left, right = new[:2], new[1:]
        new_pairs_count[left] += pairs_count[r]
        new_pairs_count[right] += pairs_count[r]
        char_count[prules[r]] += pairs_count[r]

    pairs_count = new_pairs_count

print(max(char_count.values()) - min(char_count.values()))
