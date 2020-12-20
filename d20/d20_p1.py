import re

number_in_input = re.compile(r'\d+')
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

def match_by_rotation(image_1, image_2):
    for i in range(1,5):
        if image_1[0] == image_2[0]: 
            return True
        elif image_1[-1] == image_2[-1]: 
            return True
        elif [image_1[k][0] for k in range(len(image_1))] == [image_2[k][0] for k in range(len(image_2))]: 
            return True
        elif [image_1[k][-1] for k in range(len(image_1))] == [image_2[k][-1] for k in range(len(image_2))]: 
            return True
        image_1 = rotate(image_1)
    return False

def match(image_1, image_2):
    mr = match_by_rotation(image_1, image_2)
    if mr: return True
    image_1 = flip(image_1)
    mr = match_by_rotation(image_1, image_2)
    if mr: return True
    return False

def pretty_print(image):
    for row in image:
        print(row)

for tile in tiles:
    tile['matches'] = []

for i, tile_1 in enumerate(tiles):
    for j in range(i+1, len(tiles)):
        if match(tile_1['image'], tiles[j]['image']):
            tile_1['matches'].append(tiles[j]['id'])
            tiles[j]['matches'].append(tile_1['id'])

prod = 1
for tile in tiles:
    if len(tile['matches']) == 2:
        prod *= tile['id']

print(prod)
