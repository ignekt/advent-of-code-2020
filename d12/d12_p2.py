import re

f = open('input.txt')

east = 0
north = 0
waypoint = {'east': 10,  'north': 1}

def turn_right():
    global waypoint
    tmp = waypoint['north']
    waypoint['north'] = -waypoint['east']
    waypoint['east'] = tmp

def turn_left():
    global waypoint
    tmp = waypoint['north']
    waypoint['north'] = waypoint['east']
    waypoint['east'] = -tmp

def update_location(n):
    global waypoint, east, north
    east += n * waypoint['east']
    north += n * waypoint['north']

for line in f:
    m = re.match(r'([S|W|E|N|F|R|L]{1})(\d+)', line[:-1])
    instruction = (m.group(1), int(m.group(2)))
    if instruction[0] == 'F':
        update_location(instruction[1])
    elif instruction[0] == 'R': 
        times = int(instruction[1] / 90)
        for time in range(times):
            turn_right()
    elif instruction[0] == 'L': 
        times = int(instruction[1] / 90)
        for time in range(times):
            turn_left()
    elif instruction[0] == 'E': 
        waypoint['east'] += instruction[1]
    elif instruction[0] == 'W': 
        waypoint['east'] -= instruction[1]
    elif instruction[0] == 'S': 
        waypoint['north'] -= instruction[1]
    else: waypoint['north'] += instruction[1]

print(abs(north) + abs(east))
