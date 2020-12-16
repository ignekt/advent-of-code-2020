f = open('input.txt')

numbers = []

for i in range(25):
    numbers.append(int(f.readline()))

flag = False
for line in f:
    new = int(line[:-1])
    flag = True
    for num in numbers:
        if new - num in numbers and new - num != num:
            numbers = numbers[1:]
            numbers.append(new)
            flag = False
            break
    if flag: 
        print(new)
        break
