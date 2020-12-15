import re

f = open('input.txt')

bag = re.compile(r'^\s*\d*\s?(?P<bag>[a-z]+\s[a-z]+)')

dictio = {}

def search(key):
    global dictio
    if key == 'no other': return 0
    if 'shiny gold' in dictio[key]: return 1
    for inside in dictio[key]:
        if search(inside): return 1
    return 0

for line in f:
    tmp = line[:-1].split('contain')
    container = bag.match(tmp[0]).group('bag')
    dictio[container] = []
    for info in tmp[1].split(','):
        dictio[container].append(bag.match(info).group('bag'))

s = 0
for key in dictio:
    s += search(key)

print(s)
