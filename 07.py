with open('./inp/07.txt') as f:
    crabs = list(sorted(map(int, f.read().split(','))))

# Part A
get_total_distance_from = lambda crabs, n: sum(abs(i - n) for i in crabs)
print(min(get_total_distance_from(crabs, i) for i in range(min(crabs), max(crabs) + 1)))

# Part B
get_distance_for = lambda n: (n*(n+1)) // 2
get_total_distance_from = lambda crabs, n: sum(get_distance_for(abs(i-n)) for i in crabs)
print(min(get_total_distance_from(crabs, i) for i in range(min(crabs), max(crabs) + 1)))