# constants
NUM_ROWS = 7
NUM_COLS = 3

# read input data
with open('./data/data-5.txt','r') as data_file:
     data = data_file.readlines() 

seat_indices = []
for line in data:
    # get seat row index
    row = 0
    power = NUM_ROWS - 1
    for i in range(NUM_ROWS):
        if line[i] == 'B':
            row = row + 2**power
        power = power - 1

    # get seat column index
    column = 0
    power = NUM_COLS - 1
    for i in range(NUM_COLS):
        if line[NUM_ROWS + i] == 'R':
            column = column + 2**power
        power = power - 1

    # append seat index to list
    seat_indices.append(row * (NUM_ROWS + 1) + column)

# print answer
seat_indices.sort()
previous_index = seat_indices[0]
for seat_index in seat_indices[1:]:
    if seat_index - previous_index == 2:
        print('Answer: ' + str(seat_index - 1))
        break
    previous_index = seat_index

