f = open('./input.txt', 'r')
input = f.read().splitlines()
f.close()

p1 = int(input[0].split(':')[-1])
p2 = int(input[1].split(':')[-1])

s1 = 0
s2 = 0

hody = 0
hodeni = 0

while True:
    hody += 1
    hodeni += 1
    kroky = sum([hody * 3 - 2, hody * 3 -1, hody * 3])
    if hody == 100:
        hody = 0
    if hodeni % 2 == 0:
        p2 += kroky
        p2 = p2 % 10
        if p2 == 0:
            p2 = 10
        s2 += p2
        if s2 >= 1000:
            break
    else:
        p1 += kroky
        p1 = p1 % 10
        if p1 == 0:
            p1 = 10
        s1 += p1
        if s1 >= 1000:
            break

winner = 3 * hodeni * min(s1,s2)
print(f'Prva cast vysledok: {winner}')


p1 = int(input[0].split(':')[-1])
p2 = int(input[1].split(':')[-1])

memory = {}
def compute_winner(s1, s2, p1, p2, turn):
    if s1 >= 21:
        return (1,0)
    if s2 >= 21:
        return (0,1)
    if (s1, s2, p1, p2, turn) in memory:
        return memory[(s1, s2, p1, p2, turn)]
    vysledky = (0,0)
    for d1 in [1,2,3]:
        for d2 in [1,2,3]:
            for d3 in [1,2,3]:
                if turn == 1:
                    new_p1 = (p1 + d1 + d2 + d3) % 10
                    if new_p1 == 0:
                        new_p1 = 10
                    new_s1  = s1 + new_p1
                    x, y = compute_winner(new_s1, s2, new_p1, p2, 2)
                    vysledky = (vysledky[0] + x, vysledky[1]+y)
                else:
                    new_p2 = (p2 + d1 + d2 + d3) % 10
                    if new_p2 == 0:
                        new_p2 = 10
                    new_s2  = s2 + new_p2
                    x, y = compute_winner(s1, new_s2, p1, new_p2, 1)
                    vysledky = (vysledky[0] + x, vysledky[1]+y)
    memory[(s1, s2, p1, p2, turn)] = vysledky
    return vysledky
vysledky = compute_winner(0, 0, p1, p2, 1)

print(f'Druha cast vysledok: {max(vysledky)}')
