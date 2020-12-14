f = open('input.txt')

grid = [line[:-1] for line in f.readlines()]

def count(right, down):
    global grid
    bound = len(grid[0])
    trees = 0
    row, column = 0, right
    while row+down < len(grid):
        if grid[row+down][column % bound] == '#': trees += 1
        row += down
        column += right
    return trees

print(count(3,1)*count(1,1)*count(5,1)*count(7,1)*count(1,2))
