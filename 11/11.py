f = open('./input.txt', 'r')
input = f.read().splitlines()
f.close()

SIZE = 10

def make_grid(input):
    grid = []
    for row in input:
        octos = []
        for oct in row:
            octos.append(int(oct))
        grid.append(octos)
    return grid

grid = make_grid(input)

def run_step(grid):
    for i in range(SIZE):
        for j in range(SIZE):
            grid[i][j] += 1
    flash = True
    flashed = []
    while flash:
        flash = False
        for i in range(SIZE):
            for j in range(SIZE):
                v = grid[i][j]
                if v > 9 and (i,j) not in flashed:
                    flash = True
                    flashed.append((i,j))
                    if i > 0:
                        grid[i-1][j] += 1
                    if j > 0:
                        grid[i][j-1] += 1
                    if j < SIZE -1:
                        grid[i][j+1] += 1
                    if i < SIZE -1:
                        grid[i+1][j] += 1

                    # diagonal
                    if i > 0 and j > 0:
                        grid[i-1][j-1] += 1
                    if i > 0 and j < SIZE -1:
                        grid[i-1][j+1] += 1
                    if i < SIZE -1 and j < SIZE -1:
                        grid[i+1][j+1] += 1
                    if i < SIZE -1 and j > 0:
                        grid[i+1][j-1] += 1
    for i,j in flashed:
        grid[i][j] = 0

    return grid, len(flashed)

count = 0
for step in range(100):
    grid, flashed = run_step(grid)
    count += flashed

print(f'Prva cast vysledok: {count}')

grid = make_grid(input)

def has_all_flashed(grid):
        vsetky = True
        for i in range(SIZE):
            for j in range(SIZE):
                if grid[i][j] != 0:
                    vsetky = False
        return vsetky

step = 1
while True:
    grid, _ = run_step(grid)
    if has_all_flashed(grid):
        break
    step += 1

print(f'Druha cast vysledok: {step}')
