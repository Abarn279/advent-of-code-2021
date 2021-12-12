from collections import deque

with open('./inp/10.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

pairs = {'{': '}', '[': ']', '(': ')', '<': '>'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}

# Part A
sm = 0
incomplete = [] 
for line in inp:
    stack = deque()

    for c in line: 
        if c in '({<[':
            stack.appendleft(c)
        elif c in ')}>]':
            t = stack.popleft()
            if pairs[t] != c:
                sm += points[c]
    
print(sm)

# Part B
completion_points = {')': 1, ']': 2, '}': 3, '>': 4}
completion_scores = []
for line in inp:
    stack = deque()
    valid = True
    for c in line: 
        if c in '({<[':
            stack.appendleft(c)
        elif c in ')}>]':
            t = stack.popleft()
            if pairs[t] != c:
                valid = False
                break

    if valid: 
        completion_string = "".join(pairs[i] for i in stack)
        score = 0
        for c in completion_string:
            score *= 5
            score += completion_points[c]
        completion_scores.append(score)

print(sorted(completion_scores)[len(completion_scores) // 2])

