from utils import get_data


def is_valid_1(passport):
    passport = passport.replace('\n', ' ')
    terms = {}
    for term in passport.split(" "):
        terms[term.split(':')[0].strip()] = term.split(':')[1].strip()

    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    if required - set(terms):
        return False
    else:
        return True


TERM_PARAMS = {
    "byr": lambda x: int(x) in range(1920, 2003),
    "iyr": lambda x: int(x) in range(2010, 2021),
    "eyr": lambda x: int(x) in range(2020, 2031),
    "hgt": lambda x: ("in" == x[-2:] and int(x[:-2]) in range(59, 77)) or ("cm" == x[-2:] and int(x[:-2]) in range(150, 194)),
    "hcl": lambda x: x[0] == "#" and len(x) == 7 and int(x[1:], 16) >= 0,
    "ecl": lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    "pid": lambda x: len(x) == 9 and int(x) >= 0,
    "cid": lambda x: True
}


def is_valid_2(passport):
    terms = {}
    for term in passport.split():
        terms[term.split(':')[0].strip()] = term.split(':')[1].strip()

    try:
        for term, value in terms.items():
            if not TERM_PARAMS[term](value):
                return False

    except ValueError:
        return False

    return True


data = get_data("04")
passports = data.strip().split('\n\n')


count = 0
for passport in passports:
    if is_valid_1(passport):
        count += 1

print('part 1: {}'.format(count))


count = 0
for passport in passports:
    if is_valid_1(passport) and is_valid_2(passport):
        count += 1

print('part 2: {}'.format(count))
