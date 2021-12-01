f = open('./1_input.txt', 'r')

raw_input = f.read().splitlines()
raw_input = [int(i) for i in raw_input]

ups = 0

for i in range(len(raw_input[:-1])):
    if raw_input[i+1] > raw_input[i]:
        ups += 1

print(f'Prva cast vysledok: {ups}')

ups = 0
i = 0

while len(raw_input[i:]) >= 3:
    window_b = raw_input[i+1:i+4]
    window_a = raw_input[i:i+3]
    if sum(window_b) > sum(window_a):
        ups += 1
    i += 1

print(f'Druha cast vysledok: {ups}')
