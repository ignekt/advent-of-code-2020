f = open('input.txt')

time = int(f.readline()[:-1])

busses = [int(bus) for bus in f.readline()[:-1].split(',') if bus != 'x']

pick = None
min_wait = 100000000

for bus in busses:
    wait = (int(time / bus) * bus + bus) - time
    if wait < min_wait:
        pick = bus
        min_wait = wait

print(pick * min_wait)
