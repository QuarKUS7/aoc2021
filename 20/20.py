f = open('./input.txt', 'r')
input = f.read().splitlines()
f.close()

def bin_to_num(b):
    return int(b, 2)

PADDING = 110

algo = []
image = []
image_part = False
for row in input:
    if row == '':
        image_part = True
        continue
    if image_part:
        image.append(row)
    else:
        algo.extend(list(row))

pad = [len(image[0]) * '.']
top_pad = PADDING//2 * pad
image = top_pad + image + top_pad
padded_image = []
pad = ['.' * (PADDING//2)]

padded_image = []
for row in image:
    padded_row = pad[0] + row + pad[0]
    padded_image.append(padded_row)

m = len(padded_image[0])
n = len(padded_image)

def compute_pixel(grid, pos, algo):
    i, j = pos

    if i > 0 and j > 0 and j < m - 1 and i < n - 1:
        enhan = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + \
                grid[i][j-1] + grid[i][j] + grid[i][j+1] + \
                grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
        enhan = enhan.replace('.','0')
        enhan = enhan.replace('#','1')
        dec = bin_to_num(enhan)
        return algo[dec]
    return None


def enhance(padded_image, new_image):
    for i in range(n):
        for j in range(m):
            new_pix = compute_pixel(padded_image, (i,j), algo)
            if new_pix:
                new_image[i][j] = new_pix

    return new_image

for step in range(2):
    if padded_image[0][0] == '.':
        new_image = [[algo[0]] * m for _ in range(n)]
    else:
        new_image = [[algo[-1]] * m for _ in range(n)]
    padded_image = enhance(padded_image, new_image)

count = 0
for row in padded_image:
    for item in row:
        if item == '#':
            count += 1

print(f'Prva cast vysledok: {count}')

for step in range(48):
    if padded_image[0][0] == '.':
        new_image = [[algo[0]] * m for _ in range(n)]
    else:
        new_image = [[algo[-1]] * m for _ in range(n)]
    padded_image = enhance(padded_image, new_image)

count = 0
for row in padded_image:
    for item in row:
        if item == '#':
            count += 1

print(f'Druha cast vysledok: {count}')
