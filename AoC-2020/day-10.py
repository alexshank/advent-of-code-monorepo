from collections import defaultdict

# read input data
with open('./data/data-10.txt','r') as data_file:
     data = data_file.readlines()

# parse data into ints and sort them
data = [int(d) for d in data]
data.sort()
data.insert(0, 0)           # add zero as first entry
data.append(data[-1] + 3)   # add final joltage to list

# count the number of 1 and 3 joltage conversion differences
diff_1_count = 0
diff_3_count = 0
for i in range(1, len(data)):
    diff = data[i] - data[i-1]
    if diff == 1: diff_1_count += 1
    if diff == 3: diff_3_count += 1

# print first answer
print('Answer: ' + str(diff_1_count * diff_3_count))

# sum the ways you could reach each number within 3
# of the current number (running sum)
def previous_three(data, ways_to_arrive, index):
    result = 0
    for i in range(1,4):
        if index - i >= 0 and data[index] - data[index - i] <= 3:
            result += ways_to_arrive[index - i]
    return result

# count unique paths that complete joltage conversion
# (see README for solution I had to look at)
ways_to_arrive = [1] * len(data)
for i in range(1, len(data)):
    ways_to_arrive[i] = previous_three(data, ways_to_arrive, i)

# print second answer
print('Answer: ' + str(ways_to_arrive[-1]))