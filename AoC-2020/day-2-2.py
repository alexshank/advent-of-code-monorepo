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
for policy, password in zip(policies, passwords):
    # get indices needed to find min, max, and char
    dash_index = policy.index('-')
    space_index = policy.index(' ')

    # get min, max, and char
    minimum = int(policy[:dash_index])
    maximum = int(policy[dash_index+1:space_index])
    char = policy[-1]

    # inputs are not zero-indexed
    minimum = minimum - 1
    maximum = maximum - 1

    # check if password is valid 
    sub_count = 0
    if minimum < len(password) and password[minimum] == char:
        sub_count = sub_count + 1
    if maximum < len(password) and password[maximum] == char:
        sub_count = sub_count + 1
    if sub_count == 1:
        valid_count = valid_count + 1

# print result
print('Answer: ' + str(valid_count))