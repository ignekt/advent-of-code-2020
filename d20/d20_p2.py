import re

f = open('input.txt')

tiles = []
count = 0
for line in f:
    if line == '\n':
        count += 1
        continue
    if 'Tile' in line[:-1]: 
        tiles.append({})
        tiles[count]['id'] = int(re.match(r'.*?(\d+).*?', line[:-1]).group(1))
        tiles[count]['image'] = []
    else: tiles[count]['image'].append(line[:-1])

def flip(image):
    new_image = []
    for row in image:
        new_image.append(row[::-1])
    return new_image

def rotate(image):
    new_image = []
    for column in range(len(image[0])):
        new_row = ''
        for row in range(len(image)):
            new_row += image[row][column]
        new_image.append(new_row[::-1])
    return new_image

def side(image_1, image_2):
    if image_1[0] == image_2[-1]: 
        return 'up'
    elif image_1[-1] == image_2[0]: 
        return 'down'
    elif [image_1[k][0] for k in range(len(image_1))] == [image_2[k][-1] for k in range(len(image_2))]: 
        return 'left'
    elif [image_1[k][-1] for k in range(len(image_1))] == [image_2[k][0] for k in range(len(image_2))]: 
        return 'right'
    return False

def match(image_1, image_2):
    fl = ['yes', 'no']
    rot = ['one', 'two', 'three', 'zero']
    for y in fl:
        image_2 = flip(image_2)
        for t in rot:
            image_2 = rotate(image_2)
            s = side(image_1, image_2)
            if s:
                return (image_1, image_2, s)
    return False

def pretty_print(image):
    for row in image:
        print(row)

def get_tile_by_id(iden):
    for tile in tiles:
        if tile['id'] == iden:
            return tile

def reverse_direction(direction):
    if direction == 'up': return 'down'
    elif direction == 'right': return 'left'
    elif direction == 'down': return 'up'
    else: return 'right'

for tile in tiles:
    tile['matches'] = 0  

ref = None

for i, tile_1 in enumerate(tiles):
    for j in range(i+1, len(tiles)):
        o = match(tile_1['image'], tiles[j]['image'])
        if o:
            tile_1['matches'] += 1
            tiles[j]['matches'] += 1
    if tile_1['matches'] == 2: 
        ref = tile_1
        break

for tile in tiles:
    tile['matches'] = []

tiles_queue = [ref]
searched = []
while tiles_queue:
    current_tile = tiles_queue.pop()
    for tile in [t for t in tiles if t not in searched]:
        if tile['id'] != current_tile['id']:
            o = match(current_tile['image'], tile['image'])
            if o:
                tile['image'] = o[1] 
                current_tile['matches'].append((tile['id'], o[2]))
                tile['matches'].append((current_tile['id'], reverse_direction(o[2])))
                tiles_queue.append(tile)
    searched.append(current_tile)

ref = None
for tile in tiles:
    directions = [m[1] for m in tile['matches']]
    if sorted(['down', 'right']) == sorted(directions):
        ref = tile
        break

image = []
row = ref

for tile in tiles:
    tile['image'] = tile['image'][1:-1]
    tile['image'] = [k[1:-1] for k in tile['image']]

while row:
    new_row = None
    image_row = None
    column = row
    flag = True
    while column:
        if flag:
            for m in column['matches']:
                if m[1] == 'down':
                    new_row = get_tile_by_id(m[0])
                    flag = False
                    break
        new_column = None
        if not image_row:
            image_row = column['image']
        else:
            for i in range(len(column['image'])):
                image_row[i] += column['image'][i]
        for m in column['matches']:
            if m[1] == 'right':
                new_column = get_tile_by_id(m[0])
                break
        column = new_column
    row = new_row
    if not image:
        image = image_row
    else:
        for i in range(len(image_row)):
            image.append(image_row[i])

max_monsters = 0
fl = ['yes', 'no']
rot = ['one', 'two', 'three', 'zero']
for y in fl:
    image = flip(image)
    for t in rot:
        monsters = 0
        image = rotate(image)
        for i in range(len(image)-3):
            for j in range(len(image[0])-20):
                s = ''
                for k in range(3):
                    s += image[i+k][j:j+20]
                if re.match(r'(^.{18}#.{1}#.{4}##.{4}##.{4}###.#.{2}#.{2}#.{2}#.{2}#.{2}#.{3})', s): monsters += 1
            if monsters > max_monsters:
                max_monsters = monsters

count = 0
for row in image:
    count += row.count('#')

print(count - max_monsters * 15)
