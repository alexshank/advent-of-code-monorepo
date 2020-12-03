# read input data
with open('./data/data-2.txt','r') as data_file:
     data = data_file.readlines() 

# split data into policies and passwords 
policies = []
passwords = []
for line in data:
    policy, password = line.split(': ')
    policies.append(policy)
    passwords.append(password[:-1]) # remove newline character

# count valid passwords
valid_count = 0
for i in range(len(passwords)):
    # get indices needed to find min, max, and char
    dash_index = policies[i].index('-')
    space_index = policies[i].index(' ')

    # get min, max, and char
    minimum = int(policies[i][:dash_index])
    maximum = int(policies[i][dash_index+1:space_index])
    char = policies[i][-1]

    # check if password is valid 
    char_count = passwords[i].count(char)
    if minimum <= char_count and char_count <= maximum:
        valid_count = valid_count + 1

# print result
print('Answer: ' + str(valid_count))