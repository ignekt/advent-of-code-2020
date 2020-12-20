import copy

f = open('input.txt')

grid = []
new_grid = []
length = 0
widht = 0

def direction(i, j, i_inc, j_inc):
    global grid, length, width
    i = i + i_inc
    j = j + j_inc
    while i < width and i >= 0 and j < length and j >= 0:
        if grid[i][j] == '#': return 1
        elif grid[i][j] == 'L': return 0
        i = i + i_inc
        j = j + j_inc
    return 0

def neighbours(i, j):
    global grid, length, width
    directions = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)]
    occupied = 0
    for i_inc, j_inc in directions:
        occupied += direction(i, j, i_inc, j_inc)
    return occupied

def update_seat(i, j):
    global grid, new_grid
    if grid[i][j] == 'L' and not neighbours(i, j):
        new_grid[i][j] = '#'
    elif grid[i][j] == '#' and neighbours(i, j) >= 5:
        new_grid[i][j] = 'L'

def update():
    global length, width
    for i in range(width):
        for j in range(length):
            update_seat(i, j)

def count():
    global new_grid, length, width
    c = 0 
    for i in range(width):
        for j in range(length):
            if new_grid[i][j] == '#': c += 1
    return c

for line in f:
    grid.append([letter for letter in line[:-1]])

length = len(grid[0])
width = len(grid)

while True:
    new_grid = copy.deepcopy(grid)
    update()
    if grid == new_grid: 
        print(count())
        break
    grid = new_grid
