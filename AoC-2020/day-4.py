# required fields
REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# read input data
with open('./data/data-4.txt','r') as data_file:
     data = data_file.readlines() 

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
for passport in passports:
    # remove value from passport kv_pairs
    fields = [kv_pair[:3] for kv_pair in passport]

    # check if all required fields are present
    valid = True
    for required_field in REQUIRED_FIELDS:
        if required_field in fields:
            continue
        else:
            valid = False
            break

    # update valid count
    if valid == True:
        valid_count = valid_count + 1

# print answer
print('Answer: ' + str(valid_count))