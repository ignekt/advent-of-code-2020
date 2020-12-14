f = open('input.txt')

passports = []
passport = {}

def validate(passport):
    required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for field in required:
        if field not in passport:
            return False
    return True

for line in f.readlines():
    if line == '\n':
        passports.append(passport)
        passport = {}
        continue
    for elem in line[:-1].split():
        key, value = elem.split(":")
        passport[key] = value

if passport: passports.append(passport)

count = 0
for passport in passports:
    if validate(passport): count += 1

print(count)
