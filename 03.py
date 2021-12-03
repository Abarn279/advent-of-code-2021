with open('./inp/03.txt') as f:
    diag = [line.rstrip() for line in f.readlines()]
    digits = ["".join(i) for i in zip(*diag)]
    num_digits = len(digits)

# Part A
gr = 0
for d in digits:
    gr = gr << 1                            # shift left. first iteration won't matter since it starts at 0.
    common = int(max(d, key=d.count))       # get most common element for this digit, either 1 or 0
    gr = gr | common                        # or it in on the empty last digit of our gr.

er = ~gr & (0xFFFFFFFF >> 32 - num_digits)  # negate, then mask to only get number of digits required.
print(er * gr)

# Part B
possible_or = diag[:]
possible_c02 = diag[:]

for dn in range(len(digits)):
    bits_for_digit_remaining = ["".join(i) for i in zip(*possible_or)][dn]
    common = '1' if bits_for_digit_remaining.count('1') >= bits_for_digit_remaining.count('0') else '0'
    possible_or = [i for i in possible_or if i[dn] == common]
    if len(possible_or) == 1: break

for dn in range(len(digits)):
    bits_for_digit_remaining = ["".join(i) for i in zip(*possible_c02)][dn]
    common = '0' if bits_for_digit_remaining.count('1') >= bits_for_digit_remaining.count('0') else '1'
    possible_c02 = [i for i in possible_c02 if i[dn] == common]
    if len(possible_c02) == 1: break

print(int(possible_or[0], 2) * int(possible_c02[0], 2))