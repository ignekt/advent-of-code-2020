f = open('input.txt')

def find(groups):
    su = 0
    for group in groups:
        su += len(set(group))
    return su

groups = []
current = []
for line in f:
    if line == '\n':
        groups.append(current)
        current = []
        continue
    for letter in line[:-1]:
        current.append(letter)

if current: groups.append(current)

print(find(groups))
