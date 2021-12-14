f = open('./input.txt', 'r')
input = f.read().splitlines()
f.close()

from collections import defaultdict

template = input[0]

rules = {}
for row in input[2:]:
    row = row.split(' -> ')
    rules[row[0]] = row[1]

pairs = defaultdict(lambda:0)
for i in range(len(template)-1):
    pairs[template[i:i+2]] += 1

def make_step(pairs):
    new_pairs = defaultdict(lambda:0)
    for pair in pairs:
        if pair in rules:
            next_pairs = (pair[0] + rules[pair], rules[pair] + pair[1])
            for new_pair in next_pairs:
                new_pairs[new_pair] += pairs[pair]
        else:
            new_pairs[pair] += pairs[pair]
    return new_pairs

def compute_result(pairs):
    char_count = defaultdict(lambda:0)
    for pair in pairs:
        char_count[pair[0]] += pairs[pair]

    char_count[template[-1]] += 1

    occurences = list(char_count.values())
    occurences.sort(key=lambda tup: tup)

    return occurences[-1] - occurences[0]

part_one = pairs.copy()
for step in range(10):
    part_one = make_step(part_one)
result = compute_result(part_one)

print(f'Prva cast vysledok: {result}')

part_two = pairs.copy()
for step in range(40):
    part_two = make_step(part_two)
result = compute_result(part_two)

print(f'Druha cast vysledok: {result}')
