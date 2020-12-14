import re

def check(m, M, c, password):
    occurences = password.count(c)
    if m <= occurences and M >= occurences:
        return True

f = open('input.txt')
p = re.compile(r'(?P<min>\d+)-(?P<max>\d+)\s(?P<char>[a-z]):\s(?P<password>[a-z0-9]+)')

count = 0
for line in f:
    m = p.search(line)
    if check(int(m.group('min')), int(m.group('max')), m.group('char'), m.group('password')):
        count += 1

print(count)
