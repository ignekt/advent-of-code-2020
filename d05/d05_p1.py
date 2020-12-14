def find_seat(descr):
    start = 0
    end = 127
    for letter in descr[:7]:
        if letter == 'F':
            end = start + int((end-start)/2)
        else:
            start = start + int((end-start)/2) + 1
    row = start

    start = 0
    end = 7
    for letter in descr[7:]:
        if letter == 'L':
            end = start + int((end-start)/2)
        else:
            start = start + int((end-start)/2) + 1
    column = start
    return row * 8 + column

f = open('input.txt')

ids = [find_seat(line[:-1]) for line in f]

print(max(ids))
