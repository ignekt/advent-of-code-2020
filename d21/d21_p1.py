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
count = 0 
for ingredient in not_allergens:
    for instruction in lst:
        if ingredient in instruction[0]:
            count += 1

print(count)
