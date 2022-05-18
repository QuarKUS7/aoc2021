version_num = 0

hex_to_bin = {'0' : '0000',
        '1' : '0001',
        '2' : '0010',
        '3' : '0011',
        '4' : '0100',
        '5' : '0101',
        '6' : '0110',
        '7' : '0111',
        '8' : '1000',
        '9' : '1001',
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111'}

f = open('./input.txt', 'r')
input = f.read().splitlines()
f.close()

bin_nums = []
for hex in input[0]:
    bin_nums.append(hex_to_bin[hex])

bin_nums = ''.join(bin_nums)

def bin_to_num(b):
    return int(b, 2)

def process_literal(pack):
    num = ''
    while True:
        stop = pack[0]
        num += pack[1:5]
        pack = pack[5:]
        if stop == '0':
            break
    return pack, bin_to_num(num)

def process_packet(pack):

    version = bin_to_num(pack[:3])

    # Not greate, not terrible
    global version_num
    version_num += version

    packet_type = bin_to_num(pack[3:6])
    pack = pack[6:]

    if packet_type == 4:
        pack, value = process_literal(pack)
        return value, pack
    else:
        values = []
        length_type = pack[0]
        pack = pack[1:]
        if length_type == '0':
            total = pack[:15]
            total = bin_to_num(total)
            pack = pack[15:]
            sub = pack[:total]
            pack = pack[total:]
            while sub:
                v, sub = process_packet(sub)
                values.append(v)
        else:
            total = pack[:11]
            total = bin_to_num(total)
            pack = pack[11:]
            for i in range(total):
                v, pack = process_packet(pack)
                values.append(v)

        if packet_type == 0: values = sum(values)
        elif packet_type == 1:
            p = 1
            for i in values:
                p *= i
            values = p
        elif packet_type == 2: values = min(values)
        elif packet_type == 3: values = max(values)
        elif packet_type == 5:
            if values[0] > values[1]:
                values = 1
            else:
                values = 0
        elif packet_type == 6:
            if values[0] < values[1]:
                values = 1
            else:
                values = 0
        elif packet_type == 7:
            if values[0] == values[1]:
                values = 1
            else:
                values = 0
        return values, pack

values, _ = process_packet(bin_nums)
print(f'Prva cast vysledok: {version_num}')
print(f'Druha cast vysledok: {values}')
