f = open('./input.txt', 'r')
input = f.read().splitlines()
f.close()

patterns = []
output_values = []

for row in input:
    row = row.split(' | ')
    patterns.append(row[0].split(' '))
    output_values.append(row[1].split(' '))

easy_numbers = 0
for row in output_values:
    for value in row:
        if len(value) in (2,3,4,7):
            easy_numbers += 1

print(f'Prva cast vysledok: {easy_numbers}')

numbers = {'123567':'0',
        '36': '1',
        '13457': '2',
        '13467': '3',
        '2346': '4',
        '12467': '5',
        '124567': '6',
        '136': '7',
        '1234567': '8',
        '123467': '9'}


def decode_segements(patterns, segments):
    jedna, styri, sedem = None, None, None
    petky = []
    setky = []
    pozname = set()
    for pattern in patterns:
        pocet = len(pattern)
        if pocet == 2:
            jedna = set(pattern)
        elif pocet == 3:
            sedem = set(pattern)
        elif pocet == 4:
            styri = set(pattern)
        elif pocet == 5:
            petka = set(pattern)
            petky.append(petka)
        elif pocet == 6:
            setka = set(pattern)
            setky.append(setka)
    segments[1] = sedem - jedna
    segments[1] = segments[1].pop()
    pozname.add(segments[1])
    segments[4] = (((petky[0] & petky[1] & petky[2]) - pozname) & styri).pop()
    pozname.add(segments[4])
    segments[2] = ((styri - jedna) - set(segments[4])).pop()
    pozname.add(segments[2])
    segments[7] = ((petky[0] & petky[1] & petky[2]) - pozname).pop()
    pozname.add(segments[7])
    segments[5] = ((petky[0] ^ petky[1] ^ petky[2]) - pozname).pop()
    pozname.add(segments[5])
    segments[6] = ((setky[0] ^ setky[1] ^ setky[2]) - pozname).pop()
    pozname.add(segments[6])
    segments[3] = (jedna - pozname).pop()
    return segments

sums = []
for pattern, digits in zip(patterns, output_values):
    segments = {i:None for i in range(1,8)}
    decoded_segments = decode_segements(pattern, segments)
    decoded_segments = {v: k for k, v in decoded_segments.items()}
    disp = ''
    for digit in digits:
        chars = []
        for ch in digit:
            chars.append(decoded_segments[ch])
        chars = sorted(chars)
        chars = [str(ch) for ch in chars]
        chars = ''.join(chars)
        num = numbers[chars]
        disp += num
    sums.append(int(disp))

print(f'Druha cast vysledok: {sum(sums)}')
