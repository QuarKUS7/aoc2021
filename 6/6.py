f = open('./input.txt', 'r')
init_state = f.read().splitlines()
f.close()

init_state = init_state[0].split(',')
init_lanterns = {k:0 for k in range(len(init_state))}

for lantern in init_state:
    init_lanterns[int(lantern)] += 1

def compute_lanterns(lanterns, days):
    for _ in range(days):
        new_lanterns = {}
        for lantern in range(9):
            if lantern in lanterns:
                value = lanterns[lantern]
            else:
                continue
            if lantern == 0:
                new_lanterns[8] = value
                new_lanterns[6] = value
            elif lantern == 7:
                if 6 in new_lanterns:
                    new_lanterns[6] += value
                else:
                    new_lanterns[6] = value
            else:
                lantern -= 1
                new_lanterns[lantern] = value
        lanterns = new_lanterns
    return lanterns

lanterns = compute_lanterns(init_lanterns, 80)

print(f'Prva cast vysledok: {sum(lanterns.values())}')

lanterns = compute_lanterns(init_lanterns, 256)

print(f'Druha cast vysledok: {sum(lanterns.values())}')
