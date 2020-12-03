# needed libraries
from functools import reduce

# read input data
with open('./data/data-3.txt','r') as data_file:
     data = data_file.readlines() 


# get tree indices for each line
tree_indices = []
for line in data:
    indices = [i for i, c in enumerate(line) if c == '#']
    tree_indices.append(indices)

# count tree collisions going right 3, down 1
slope_count = 5
x_positions = [0] * slope_count
y_positions = [0] * slope_count
collision_counts = [0] * slope_count
x_max = len(data[0]) - 1
x_deltas = [1, 3, 5, 7, 1]
y_deltas = [1, 1, 1, 1, 2]
for i in range(slope_count):
    while y_positions[i] < len(data):
        if x_positions[i] % x_max in tree_indices[y_positions[i]]:
            collision_counts[i] = collision_counts[i] + 1
        x_positions[i] = x_positions[i] + x_deltas[i]
        y_positions[i] = y_positions[i] + y_deltas[i]

# print result (using lambda function)
print('Answer: ' + str(reduce(lambda x, y: x*y, collision_counts)))
