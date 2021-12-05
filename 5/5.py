import collections

f = open('./input.txt', 'r')

lines = f.read().splitlines()

all_points = []

for line in lines:
    line = line.split('->')
    start = line[0].split(',')
    end = line[1].split(',')
    start = [int(s.strip()) for s in start]
    end = [int(s.strip()) for s in end]
    points = []
    if start[0] == end[0]:
        points = list(range(int(min(start[1],end[1])),int(max(start[1],end[1]))+1))
        points = [str(start[0]) + ',' + str(p) for p in points]
    elif start[1] == end[1]:
        points = list(range(int(min(start[0],end[0])), int(max(start[0],end[0]))+1))
        points = [str(p)+ ',' + str(start[1]) for p in points]

    all_points += points

overlaping = 0
c = collections.Counter(all_points).most_common()
for _, count in c:
    if count > 1:
        overlaping += 1

print(f'Prva cast vysledok: {overlaping}')

all_points = []

for line in lines:
    line = line.split('->')
    start = line[0].split(',')
    end = line[1].split(',')
    start = [int(s.strip()) for s in start]
    end = [int(s.strip()) for s in end]
    points = []
    if start[0] == end[0]:
        points = list(range(int(min(start[1],end[1])),int(max(start[1],end[1]))+1))
        points = [str(start[0]) + ',' + str(p) for p in points]
    elif start[1] == end[1]:
        points = list(range(int(min(start[0],end[0])), int(max(start[0],end[0]))+1))
        points = [str(p)+ ',' + str(start[1]) for p in points]
    else:
        a_points = list(range(int(min(start[0],end[0])), int(max(start[0],end[0]))+1))
        if start[0] < end[0]:
            a_points.reverse()
        b_points = list(range(int(min(start[1],end[1])), int(max(start[1],end[1]))+1))
        if start[1] < end[1]:
            b_points.reverse()
        points = [str(a) + ',' + str(b) for a,b in zip(a_points, b_points)]

    all_points += points

overlaping = 0
counter = collections.Counter(all_points).most_common()
for _, count in counter:
    if count > 1:
        overlaping += 1

print(f'Druha cast vysledok: {overlaping}')
