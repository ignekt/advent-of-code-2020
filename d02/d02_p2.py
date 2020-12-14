import re

def check(pos1, pos2, c, password):
    if password[pos1-1] == c and not password[pos2-1] == c:
        return True
    elif password[pos2-1] == c and not password[pos1-1] == c:
        return True

f = open('input.txt')
p = re.compile(r'(?P<pos1>\d+)-(?P<pos2>\d+)\s(?P<char>[a-z]):\s(?P<password>[a-z0-9]+)')

count = 0
for line in f:
    m = p.search(line)
    if check(int(m.group('pos1')), int(m.group('pos2')), m.group('char'), m.group('password')):
        count += 1

print(count)
