f = open('./input.txt', 'r')
input = f.read().split(',')
f.close()

positions = [int(i) for i in input]

from statistics import median
stred = median(positions)

movements = int(sum([abs(stred - pos) for pos in positions]))
print(f'Prva cast vysledok: {movements}')

min_pos = min(positions)
max_pos = max(positions)
fuel = 999999999999999

for i in range(min_pos, max_pos):
    movements = 0
    for pos in positions:
        distance = abs(pos - i)
        movements += (distance * (distance + 1)) / 2
    if movements < fuel:
        fuel = movements

print(f'Druha cast vysledok: {int(fuel)}')
