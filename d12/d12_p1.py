import re

f = open('input.txt')

east = 0
north = 0
facing = 'east'

def turn_right(direction):
    if direction == 'east': return 'south'
    elif direction == 'south': return 'west'
    elif direction == 'west': return 'north'
    else: return 'east'

def turn_left(direction):
    if direction == 'east': return 'north'
    elif direction == 'south': return 'east'
    elif direction == 'west': return 'south'
    else: return 'west'

for line in f:
    m = re.match(r'([S|W|E|N|F|R|L]{1})(\d+)', line[:-1])
    instruction = (m.group(1), int(m.group(2)))
    if instruction[0] == 'F':
        if facing == 'east': east += instruction[1]
        elif facing == 'west': east -= instruction[1]
        elif facing == 'north': north += instruction[1]
        elif facing == 'south': north -= instruction[1]
    elif instruction[0] == 'R': 
        times = int(instruction[1] / 90)
        for time in range(times):
            facing = turn_right(facing)
    elif instruction[0] == 'L': 
        times = int(instruction[1] / 90)
        for time in range(times):
            facing = turn_left(facing)
    elif instruction[0] == 'E': east += instruction[1]
    elif instruction[0] == 'W': east -= instruction[1]
    elif instruction[0] == 'S': north -= instruction[1]
    else: north += instruction[1]

print(abs(north) + abs(east))
