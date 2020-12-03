# read input data
with open('./data/data-3.txt','r') as data_file:
     data = data_file.readlines() 


# get tree indices for each line
tree_indices = []
for line in data:
    indices = [i for i, c in enumerate(line) if c == '#']
    tree_indices.append(indices)

# count tree collisions going right 3, down 1
x = 0
y = 0
x_max = len(data[0]) - 1
collision_count = 0
while y < len(data):
    if x % x_max in tree_indices[y]:
        collision_count = collision_count + 1
    x = x + 3
    y = y + 1

# print result
print('Answer: ' + str(collision_count))
