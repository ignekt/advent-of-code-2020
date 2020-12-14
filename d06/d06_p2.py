f = open('input.txt')

def find(groups):
    su = 0
    for group in groups:
        for answer in set(group[1]):
            if group[1].count(answer) == group[0]:
                su += 1
    return su

groups = []
current = []
count = 0
for line in f:
    if line == '\n':
        groups.append((count, current))
        current = []
        count = 0
        continue
    for letter in line[:-1]:
        current.append(letter)
    count += 1

if current: groups.append((count,current))

print(find(groups))
