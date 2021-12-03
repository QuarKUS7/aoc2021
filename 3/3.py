import collections

f = open('./input.txt', 'r')

report = f.read().splitlines()

gamma_rate_list = []
epsilon_rate_list = []

for value in zip(*report):
    counter = collections.Counter(value)
    most_common = counter.most_common(2)
    gamma_rate_list.append(most_common[0][0])
    epsilon_rate_list.append(most_common[1][0])

gamma_rate = int(''.join(gamma_rate_list), 2)
epsilon_rate = int(''.join(epsilon_rate_list), 2)

print(f'Prva cast vysledok: {gamma_rate * epsilon_rate}')

report_oxy = report.copy()
zeros = []
ones = []
bit_position = 0

while len(report_oxy) != 1:
    for value in report_oxy:
        if value[bit_position] == '0':
            zeros.append(value)
        else:
            ones.append(value)

    if len(ones) >= len(zeros):
        report_oxy = ones
    else:
        report_oxy = zeros

    bit_position += 1
    zeros = []
    ones = []

oxygen = report_oxy

report_co2 = report.copy()
zeros = []
ones = []
bit_position = 0

while len(report_co2) != 1:
    for value in report_co2:
        if value[bit_position] == '0':
            zeros.append(value)
        else:
            ones.append(value)

    if len(ones) >= len(zeros):
        report_co2 = zeros
    else:
        report_co2 = ones

    bit_position += 1
    zeros = []
    ones = []

co2 = report_co2

oxygen = int(''.join(oxygen[0]), 2)
co2 = int(''.join(co2[0]), 2)

print(f'Druha cast vysledok: {oxygen * co2}')
