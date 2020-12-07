import string

# required fields
REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

# read input data
input_string = './data/data-4.txt'
# input_string = './data/data-4-invalid.txt'
# input_string = './data/data-4-valid.txt'
with open(input_string,'r') as data_file:
     data = data_file.readlines() 

# validate that all needed fields are present
def validate_fields(passport):
    # need at least 7 fields to possibly be valid
    if len(passport) < 7:
        return False
    # if 7 fields, cid can't be one
    elif len(passport) == 7:
        fields = [field[:3] for field in passport]
        if 'cid' in fields:
           return False
    return True

# check that string is all digits
def isAllDigits(string):
    for l in string:
        if not l.isdigit():
            return False
    return True

# validate hair color value
def validate_hair_color(value):
    if len(value) != 7: return False
    for l in value[1:]:
        if not l in string.hexdigits:
            return False
    return True 

# validate an indiviudal field and its value
def validate_value(key, value):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if key == 'byr':
        return int(value) >= 1920 and int(value) <= 2002
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    elif key == 'iyr':
        return int(value) >= 2010 and int(value) <= 2020
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    elif key == 'eyr':
        return int(value) >= 2020 and int(value) <= 2030
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    elif key == 'hgt':
        if len(value) < 4: return False
        is_cm = value[-2:] == 'cm'
        is_in = value[-2:] == 'in'
        if is_cm:
            return int(value[:-2]) >= 150 and int(value[:-2]) <= 193
        elif is_in:
            return int(value[:-2]) >= 59 and int(value[:-2]) <= 76 
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    elif key == 'hcl':
        return validate_hair_color(value)
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    elif key == 'ecl':
        return value in EYE_COLORS
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    elif key == 'pid':
        return len(value) == 9 and isAllDigits(value)
    elif key == 'cid':
        return True

    # invalid field passed in
    return False 

# check all combinations of sums
passports = []
kv_pairs = []
for line in data:
    # add line to list of current passport's fields
    if len(line) > 1:
        kv_pairs.extend(line[:-1].split(' '))
    # new passport starts after blank line
    else:
        passports.append(kv_pairs)
        kv_pairs = []

# check each required field is present 
valid_count = 0
valid = True
for passport in passports:
    # validate passport fields
    if validate_fields(passport) == False:
        valid = False 

    # valid passport values
    kv_pairs = [kv_pair.split(':') for kv_pair in passport] 
    for field, value in kv_pairs:
        if validate_value(field, value) == False:
            valid = False
            break
    
    # update valid count
    if valid == True:
        valid_count = valid_count + 1
    valid = True

# print answer
print('Answer: ' + str(valid_count))
