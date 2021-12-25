f = open('./input.txt', 'r')
input = f.read().splitlines()
f.close()

grid = []
for row in input:
    row = list(row)
    grid.append(row)
m = len(grid[0])
n = len(grid)

EAST = '>'
SOUTH = 'v'
FREE = '.'

def print_grid(grid):
    for row in grid:
        print(row)
    print('\n')

moved = True
step = 0
while moved == True:
    moved = False
    step += 1
    new_grid = [['.'] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == EAST:
                vedla = (j+1) % m
                if grid[i][vedla] == FREE:
                    new_grid[i][vedla] = EAST
                    moved = True
                else:
                    new_grid[i][j] = EAST
    for i in range(n):
        for j in range(m):
            if grid[i][j] == SOUTH:
                vedla = (i+1) % n
                if grid[vedla][j] == FREE and new_grid[vedla][j] == FREE:
                    new_grid[vedla][j] = SOUTH
                    moved = True
                elif grid[vedla][j] == '>' and new_grid[vedla][j] == FREE:
                    new_grid[vedla][j] = SOUTH
                    moved = True
                else:
                    new_grid[i][j] = SOUTH

    grid = new_grid

print(f'Prva cast vysledok: {step}')
