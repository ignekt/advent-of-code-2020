f = open('input.txt')

data = [int(num) for num in f.read().split("\n")[:-1]]

for i, num1 in enumerate(data):
    for j, num2 in enumerate(data[i+1:]):
        for num3 in data[i+j:]:
            if num1 + num2 + num3 == 2020:
                print(num1 * num2 * num3)
