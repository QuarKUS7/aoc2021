import re

f = open('./input.txt', 'r')
input = f.read().splitlines()
f.close()

r = '-?\d+'
x = re.findall(r, input[0])
x = [int(i) for i in x]
target_area = [(x[0], x[2]), (x[1], x[3])]

def make_step(position, velocity_x, velocity_y):
    position[0] += velocity_x
    position[1] += velocity_y
    if velocity_x > 0:
        velocity_x += -1
    elif velocity_x < 0:
        velocity_x += +1
    velocity_y += -1
    return position, velocity_x, velocity_y

def is_in_targe(position, target_area):
    if target_area[0][0] <= position[0] <= target_area[1][0]:
        if target_area[0][1] <= position[1] <= target_area[1][1]:
            return True
    return False

def should_end(position, target_area):
    return position[1] < target_area[0][1]


max_y = 0
all_hits = set()

for x in range(0, target_area[1][0] + 1):
    for y in range(-1000, 1000):
        max_step_y = 0
        position = [0, 0]
        velocity_x, velocity_y = x, y
        while True:
            position, velocity_x, velocity_y = make_step(position, velocity_x, velocity_y)
            if position[1] > max_step_y:
                max_step_y = position[1]
            if is_in_targe(position, target_area):
                if max_step_y > max_y:
                    max_y = max_step_y
                all_hits.add((x,y))

                break
            if should_end(position, target_area):
                break

print(f'Prva cast vysledok: {max_y}')
print(f'Druha cast vysledok: {len(all_hits)}')
