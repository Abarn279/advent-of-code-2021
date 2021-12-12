from collections import defaultdict

with open('./inp/08.txt') as f:
    entries = [line.rstrip() for line in f.readlines()]

# Part A
sm = 0
for entry in entries:
    patterns, output = entry.split(' | ') 
    patterns = patterns.split(' ')
    output = output.split(' ')
    sm += sum(1 for j in output if len(j) in [2, 3, 4, 7])
print(sm)

# Part B
summed_no = 0

digits = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
} 

for entry in entries:
    patterns, output = entry.split(' | ') 
    patterns = patterns.split(' ')
    output = output.split(' ')

    # get the count of each character. this will help us start to solve which character represents each segment
    joinedpatterns = "".join(patterns)
    char_counts = defaultdict(lambda: set()) #{i: set() for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']}
    for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        count = joinedpatterns.count(c)
        char_counts[count].add(c)

    # first, take each segment name and try to find all of its possible aliases
    segment_to_possible_aliases = {}

    # these magic numbers come from how often a given segment shows up in a given number. we only need to solve for the ones
    # that have multiple potential answers.
    segment_to_possible_aliases['a'] = set(char_counts[8])
    segment_to_possible_aliases['b'] = char_counts[6]
    segment_to_possible_aliases['c'] = set(char_counts[8])
    segment_to_possible_aliases['d'] = set(char_counts[7])
    segment_to_possible_aliases['e'] = char_counts[4]
    segment_to_possible_aliases['f'] = char_counts[9]
    segment_to_possible_aliases['g'] = set(char_counts[7])

    # this is all of the numbers that have a unique segment count
    unique_patterns = list(sorted([i for i in patterns if len(i) in [2, 3, 4, 7]], key=lambda x: len(x))) # 1, 7, 4, 8

    # check for a. neither 1 or 4 has a, so if a possible alias of a shows up here, remove it - we now know it must be c, and have solved a.
    same_chars_1_4 = set(unique_patterns[0]).intersection(set(unique_patterns[2]))
    for sc in same_chars_1_4:
        if sc in segment_to_possible_aliases['a']: segment_to_possible_aliases['a'].remove(sc)
    segment_to_possible_aliases['c'].difference_update(segment_to_possible_aliases['a'])

    # check for g, resolve for d
    same_chars_1_4_7 = set(unique_patterns[0]).union(set(unique_patterns[1])).union(set(unique_patterns[2]))
    unique_8 = set(unique_patterns[3]).difference(same_chars_1_4_7)
    for s in segment_to_possible_aliases:
        if len(segment_to_possible_aliases[s]) == 1 and max(segment_to_possible_aliases[s]) in unique_8:
            unique_8.remove(max(segment_to_possible_aliases[s]))
    segment_to_possible_aliases['g'] = unique_8
    segment_to_possible_aliases['d'].remove(max(unique_8))
    
    # now we know the alias to the segment it represents!
    alias_to_segment = {max(j): i for i, j in segment_to_possible_aliases.items()}
    
    # now that we have deduced the aliases to each real segment name, construct our final number based on the digits object
    final_no = ""
    for o in output:
        real = "".join(sorted(alias_to_segment[i] for i in o))
        final_no = final_no + str(digits[real])
    
    # FINALLY, add this to the sum
    summed_no += int(final_no)

print(summed_no)