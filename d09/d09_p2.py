f = open('input.txt')

numbers = []

l = 1492208709

numbers = []
for line in f:
    numbers.append(int(line[:-1]))

flag = False
for i in range(len(numbers)):
    if flag: break
    su = numbers[i]
    mi = numbers[i]
    ma = numbers[i]
    for j in range(i+1, len(numbers)):
        su += numbers[j]
        if numbers[j] > ma:
            ma = numbers[j]
        elif numbers[j] < mi:
            mi = numbers[j]
        if su == l:
            print(mi + ma)
            flag = True
            break
        elif su > l:
            break
