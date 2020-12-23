import re

f = open('input.txt')

def compute(mask, num):
    res = ''
    num = format(int(num), '#038b')[2:]
    for i, bit in enumerate(num):
        if mask[i] == 'X': res += bit
        elif mask[i] == '1': res += '1'
        else: res += '0'
    return int(res, 2)
        
mask = None
mem = {}
for line in f:
    if 'mask' in line:
        mask = line[:-1].split(' = ')[1]
        continue
    line = line[:-1].split(' = ')
    mem[int(re.match('mem\[(\d+).*', line[0]).group(1))] = compute(mask, line[1])

su = 0
for address in mem:
    su += mem[address]
print(su)
