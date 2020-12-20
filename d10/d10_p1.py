f = open('input.txt')

adapters = []
for line in f:
    adapters.append(int(line[:-1]))

adapters.sort()
adapters.append(adapters[-1] + 3)

differences = {}
previous = 0

for adapter in adapters:
    current_difference = adapter - previous
    if not current_difference in differences: differences[current_difference] = 0
    differences[current_difference] += 1
    previous = adapter

print(differences[1] * differences[3])
