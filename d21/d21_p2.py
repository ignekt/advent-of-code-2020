import re
import copy

f = open('input.txt')

ingredients = {}
lst = []
for line in f:
    line = line[:-2].split(' (contains ')
    ingre = line[0].split(' ')
    allergens = line[1].split(', ')
    lst.append([ingre, allergens])
    for ingredient in ingre:
        if ingredient not in ingredients: ingredients[ingredient] = []
        for allergen in allergens:
            if allergen not in ingredients[ingredient]:
                ingredients[ingredient].append(allergen)

for ingredient in ingredients:
    tmp = copy.deepcopy(ingredients[ingredient])
    for allergen in tmp:
        for instruction in lst:
            if ingredient not in instruction[0] and allergen in instruction[1] and allergen in ingredients[ingredient]:
                ingredients[ingredient].remove(allergen)

not_allergens = [ingredient for ingredient in ingredients if not ingredients[ingredient]]

for ingredient in not_allergens:
    for instruction in lst:
        if ingredient in instruction[0]:
            instruction[0].remove(ingredient)

completed = []
while True:
    current = None
    for ingredient in ingredients:
        if len(ingredients[ingredient]) == 1 and ingredient not in completed:
            current = ingredient
            break
    if current == None: break
    for ingredient in ingredients:
        if ingredient != current and ingredients[current][0] in ingredients[ingredient]:
            ingredients[ingredient].remove(ingredients[current][0])
    completed.append(current)

allergens = [ingredient for ingredient in ingredients.items() if ingredient[1]]
allergens.sort(key=lambda x: x[1][0])
for allergen in allergens:
    print(allergen[0], end=',')
