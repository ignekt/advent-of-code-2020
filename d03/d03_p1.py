f = open('input.txt')

trees = 0

for i, line in enumerate(f):
    line = line[:-1]
    if i == 0: continue
    if line[i * 3 % len(line)] == '#': trees += 1

print(trees)
