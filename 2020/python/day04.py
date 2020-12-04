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


def is_valid_2(passport):
    passport = passport.replace('\n', ' ')
    terms = {}
    for term in passport.split():
        terms[term.split(':')[0].strip()] = term.split(':')[1].strip()

    try:
        # years
        terms['byr'] = int(terms['byr'])
        if terms['byr'] not in range(1920, 2003):
            return False
        terms['iyr'] = int(terms['iyr'])
        if terms['iyr'] not in range(2010, 2021):
            return False
        terms['eyr'] = int(terms['eyr'])
        if terms['eyr'] not in range(2020, 2031):
            return False

        # height
        terms['hgt_num'] = float(terms['hgt'][:-2])
        terms['hgt_unit'] = terms['hgt'][-2:]

        if terms['hgt_unit'] == 'cm':
            if terms['hgt_num'] not in range(150, 194):
                return False

        elif terms['hgt_unit'] == 'in':
            if terms['hgt_num'] not in range(59, 77):
                return False

        else:
            return False

        # hair and eye colour
        if terms['hcl'][0] != '#':
            return False

        elif len(terms['hcl']) != 7:
            return False

        # else:
        #     # hex baby
        #     int(terms['hcl'][1:], 16)

        if terms['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False

        # passport ID
        if len(terms['pid']) != 9:
            return False
        else:
            # even if leading zeros, this should be okay
            int(terms['pid'])

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
