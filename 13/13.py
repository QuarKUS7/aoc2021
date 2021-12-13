f = open('./input.txt', 'r')
input = f.read().splitlines()
f.close()

folds = []
dots = []
for row in input:
    if ',' in row:
        x,y = row.split(',')
        dots.append((int(x), int(y)))
    elif 'fold' in row:
        row = row.split('=')
        os = row[0][-1]
        size = row[1]
        folds.append((os, int(size)))


new_dost = []
def process_fold(dots, fold):
    new_dost = []
    os, size = fold
    if os == 'x':
        for dot in dots:
            x,y = dot
            if x == size:
                continue
            elif x > size:
                tmp = size - (x - size)
                if (tmp,y) not in new_dost:
                    new_dost.append((tmp,y))
            else:
                if (x,y) not in new_dost:
                    new_dost.append((x,y))
    elif os == 'y':
        for dot in dots:
            x,y = dot
            if y == size:
                continue
            elif y > size:
                tmp = size - (y - size)
                if (x,tmp) not in new_dost:
                    new_dost.append((x,tmp))
            else:
                if (x,y) not in new_dost:
                    new_dost.append((x,y))

    return new_dost

dots = process_fold(dots, folds[0])
print(f'Prva cast vysledok: {len(dots)}')

for fold in folds[1:]:
    dots = process_fold(dots, fold)

import matplotlib.pyplot as plt

plt.scatter(*zip(*dots), s=250)
plt.gca().invert_yaxis()
plt.show()
