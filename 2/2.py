f = open('./input.txt', 'r')

commands = f.read().splitlines()

FORWARD = 'forward'
UP = 'up'
DOWN = 'down'

position = 0
depth = 0

for command in commands:
    course, volume = command.split(' ')
    volume = int(volume)

    if course == FORWARD:
        position += volume
    elif course == UP:
        depth -= volume
    elif course == DOWN:
        depth += volume
    else:
        print(f'Unexpected course {course} for command {command}')

print(f'Prva cast vysledok: {position * depth}')

position = 0
depth = 0
aim = 0

for command in commands:
    course, volume = command.split(' ')
    volume = int(volume)

    if course == FORWARD:
        position += volume
        depth += aim * volume
    elif course == UP:
        aim -= volume
    elif course == DOWN:
        aim += volume
    else:
        print(f'Unexpected course {course} for command {command}')

print(f'Druha cast vysledok: {position * depth}')
