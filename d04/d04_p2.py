import re

height = re.compile(r'^(?P<num>\d+)(?P<unit>(cm)|(in))$')
hair = re.compile(r'^#[0-9a-f]{6}$')
eye = re.compile(r'^(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)$')
pid = re.compile(r'^\d{9}$')

f = open('input.txt')

passports = []
passport = {}

def validate(passport):
    required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for field in required:
        if field not in passport:
            return False
        if field == 'byr':
            year = int(passport[field])
            if year < 1920 or year > 2002: return False
        elif field == 'iyr':
            year = int(passport[field])
            if year < 2010 or year > 2020: return False
        elif field == 'eyr':
            year = int(passport[field])
            if year < 2020 or year > 2030: return False
        elif field == 'hgt':
            m = height.match(passport[field])
            if not m: return False
            if m.group('unit') == 'cm':
                val = int(m.group('num'))
                if val < 150 or val > 193: return False
            elif m.group('unit') == 'in':
                val = int(m.group('num'))
                if val < 59 or val > 76: return False
        elif field == 'hcl':
            m = hair.match(passport[field])
            if not m: return False
        elif field == 'ecl':
            m = eye.match(passport[field])
            if not m: return False
        elif field == 'pid':
            m = pid.match(passport[field])
            if not m: return False
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
