# constants
WINDOW_SIZE = 25

# read input data
with open('./data/data-9.txt','r') as data_file:
#with open('./data/data-7-test.txt','r') as data_file:
     data = data_file.readlines()

# convert listt of numbers to int type
data = [int(d) for d in data]

# go through every value in the list
first_answer = 0
for i in range(WINDOW_SIZE + 1, len(data)):
    # create WINDOW_SIZE set of values in the total list
    window_values = data[i-WINDOW_SIZE: i]
    found = False
    # check if needed number is within the subset of values
    for j in range(WINDOW_SIZE):
        target = data[i] - window_values[j]
        if target in window_values:
            found = True
            break
    
    # print answer if needed number isn't found
    if found == False:
        first_answer = data[i]
        print('Answer: ' + str(first_answer))
        break

# sum contiguous values until first answer is calculated
for i in range(len(data)):
    # if the fist number is too large, don't try larger range
    if data[i] >= first_answer: continue

    # sum the contiguous values
    for j in range(len(data)):
        range_sum = sum(data[i:j])
        if range_sum > first_answer:
            break
        elif range_sum == first_answer:
            print('Answer: ' + str(min(data[i:j]) + max(data[i:j])))