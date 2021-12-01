with open('./inp/01.txt') as f:
    inp = list(map(int, [line.rstrip() for line in f.readlines()]))

# Part A
differences = [inp[i + 1] - inp[i] for i in range(len(inp) - 1) if inp[i + 1] - inp[i] > 0]
print(len(differences))

# Part B
get_window_measurement = lambda window: inp[window] + inp[window + 1] + inp[window + 2]
differences = [get_window_measurement(i + 1) - get_window_measurement(i) for i in range(len(inp) - 3) if get_window_measurement(i + 1) - get_window_measurement(i) > 0]
print(len(differences))