import re

f = open('input.txt')

bag = re.compile(r'^\s*(?P<num>\d*)\s?(?P<bag>[a-z]+\s[a-z]+)')

dictio = {}

def search(key):
    global dictio
    if key == 'no other': return 1
    s = 0
    for container in dictio[key]:
        s += int(container[0]) + int(container[0]) * search(container[1])
    return s

for line in f:
    tmp = line[:-1].split('contain')
    container = bag.match(tmp[0]).group('bag')
    dictio[container] = []
    for info in tmp[1].split(','):
        dictio[container].append(( bag.match(info).group('num') if bag.match(info).group('num') else '0',
            bag.match(info).group('bag')))

print(search('shiny gold'))
