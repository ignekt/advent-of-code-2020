import re

f = open('input.txt')

def transform(mask, num):
    res = ''
    for i, bit in enumerate(num):
        if mask[i] == 'X': res += 'X'
        elif mask[i] == '1': res += '1'
        else: res += bit
    return res
        
mask = None
mem = {}
def findall(mask, address):
    address = format(int(address), '#038b')[2:]
    address = transform(mask, address)
    positions = [i for i, letter in enumerate(address) if letter == 'X']
    addresses = []
    for time in range(2**address.count('X')):
        rep = format(time, '#0'+str(address.count('X')+2)+'b')[2:]
        tmp = address
        for i, char in enumerate(rep):
            tmp = tmp[:positions[i]] + char + tmp[positions[i]+1:]
        addresses.append(int(tmp,2))
    return addresses

for line in f:
    if 'mask' in line:
        mask = line[:-1].split(' = ')[1]
        continue
    line = line[:-1].split(' = ')
    addresses = findall(mask, int(re.match('mem\[(\d+).*', line[0]).group(1)))
    for address in addresses:
        mem[address] = int(line[1])

su = 0
for address in mem:
    su += mem[address]
print(su)
