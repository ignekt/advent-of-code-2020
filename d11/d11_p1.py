import copy

f = open('input.txt')

grid = []
new_grid = []
length = 0
widht = 0

def neighbours(i, j):
    global grid, length, width
    occupied = 0
    if j + 1 < length and grid[i][j+1] == '#': occupied += 1
    if j - 1 >= 0 and grid[i][j-1] == '#': occupied += 1
    if i + 1 < width and grid[i+1][j] == '#': occupied += 1
    if i - 1 >= 0 and grid[i-1][j] == '#': occupied += 1
    if j + 1 < length and i + 1 < width and grid[i+1][j+1] == '#': occupied += 1
    if j + 1 < length and i - 1 >= 0 and grid[i-1][j+1] == '#': occupied += 1
    if j - 1 >= 0 and i + 1 < width and grid[i+1][j-1] == '#': occupied += 1
    if j - 1 >= 0 and i - 1 >= 0 and grid[i-1][j-1] == '#': occupied += 1
    return occupied

def update_seat(i, j):
    global grid, new_grid
    if grid[i][j] == 'L' and not neighbours(i, j):
        new_grid[i][j] = '#'
    elif grid[i][j] == '#' and neighbours(i, j) >= 4:
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
