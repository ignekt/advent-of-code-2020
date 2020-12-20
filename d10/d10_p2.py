f = open('input.txt')
    
adapters = []

for line in f:
    adapters.append({'value': int(line[:-1]), 'ways': 0})

adapters.append({'value': 0, 'ways': 1})
adapters.sort(key=lambda x: x['value'])
adapters.append({'value': adapters[-1]['value'] + 3, 'ways': 0})

for i, adapter in enumerate(adapters):
    j = 1
    while j <= 3 and i - j >= 0:
        if adapter['value'] - adapters[i-j]['value'] <= 3:
            adapter['ways'] += adapters[i-j]['ways']
        j += 1

print(adapters[-1]['ways'])
