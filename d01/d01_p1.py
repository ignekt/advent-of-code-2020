f = open('input.txt')

data = [int(num) for num in f.read().split("\n")[:-1]]

for i, num1 in enumerate(data):
    for num2 in data[i+1:]:
        if num1 + num2 == 2020:
            print(num1 * num2)
