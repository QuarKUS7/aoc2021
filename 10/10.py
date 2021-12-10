f = open('./input.txt', 'r')
input = f.read().splitlines()
f.close()

PAIRS = {')': '(', '}': '{', '>': '<', ']': '['}
ERROR_TABLE = {')': 3, ']': 57, '}': 1197, '>': 25137}
INCOMPLETE_TABLE = {'(': 1, '[': 2, '{': 3, '<': 4}
INCOMPLETE_COEF = 5


def check_line(line):
    stack = []
    for bracket in line:
        if bracket in PAIRS.values():
            stack.append(bracket)
            continue

        if bracket not in PAIRS.keys():
            return 'corupted', bracket

        ending = stack.pop()

        if ending ==  PAIRS[bracket]:
            continue
        return 'corupted', bracket

    if stack:
        return 'incomplete', stack[::-1]

ilegals = []
incompletes = []
for line in input:
    result, values = check_line(line)

    if result == 'corupted':
        ilegals.append(values)
    else:
        incompletes.append(values)

score = 0
for ilegal in ilegals:
    score += ERROR_TABLE[ilegal]

print(f'Prva cast vysledok: {score}')

score = []
for incomplete in incompletes:
    line_score = 0
    for missing in incomplete:
        line_score *= INCOMPLETE_COEF
        line_score += INCOMPLETE_TABLE[missing]
    score.append(line_score)

import statistics
middle_score = statistics.median(score)

print(f'Druha cast vysledok: {middle_score}')
