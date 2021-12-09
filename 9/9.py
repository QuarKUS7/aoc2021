f = open('./input.txt', 'r')
input = f.read().splitlines()
f.close()

def find_low_points(input, m, n):
    low_points = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            v = int(input[i][j])
            ajacent = []
            if i > 0:
                ajacent.append(input[i-1][j])
            if j > 0:
                ajacent.append(input[i][j-1])
            if j < n -1:
                ajacent.append(input[i][j+1])
            if i < m -1:
                ajacent.append(input[i+1][j])
            if all([int(x) > v for x in ajacent]):
                low_points.append((i,j))
    return low_points

low_points = find_low_points(input, len(input), len(input[0]))
risk = 0
for i,j in low_points:
    risk += (int(input[i][j]) + 1)

print(f'Prva cast vysledok: {risk}')

def compute_basin_size(low_point, m, n):
    """BFS"""
    queue = [low_point]
    basin = 1
    seen = []
    while queue:
        i, j = queue.pop()
        v = int(input[i][j])
        if i > 0:
            point = int(input[i-1][j])
            if point > v and point != 9:
                if (i-1,j) not in seen:
                    basin += 1
                    queue.append((i-1,j))
                    seen.append((i-1,j))
        if j > 0:
            point = int(input[i][j-1])
            if point > v and point != 9:
                if (i,j-1) not in seen:
                    basin += 1
                    queue.append((i,j-1))
                    seen.append((i,j-1))
        if j < n -1:
            point = int(input[i][j+1])
            if point > v and point != 9:
                if (i,j+1) not in seen:
                    basin += 1
                    queue.append((i,j+1))
                    seen.append((i,j+1))
        if i < m -1:
            point = int(input[i+1][j])
            if point > v and point != 9:
                if (i+1,j) not in seen:
                    basin += 1
                    queue.append((i+1,j))
                    seen.append((i+1,j))
    return basin

basin_sizes = []

for low_point in low_points:
    basin_sizes.append(compute_basin_size(low_point, len(input), len(input[0])))

combined_basins = 1
for basin_size in sorted(basin_sizes)[-3:]:
    combined_basins *= basin_size

print(f'Druha cast vysledok: {combined_basins}')
