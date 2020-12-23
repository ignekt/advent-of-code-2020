f = open('input.txt')

time = int(f.readline()[:-1])

busses = [[int(bus), i] for i, bus in enumerate(f.readline()[:-1].split(',')) if bus != 'x']

product = 1

for bus in busses:
    product *= bus[0]

res = 0

for bus in busses:
    l = product / bus[0] % bus[0]
    k = 1
    tmp = l
    while l % bus[0] != 1:
        k += 1
        l = tmp * k
    res += (bus[0] - bus[1]) * (product / bus[0]) * k

print(res % product)
