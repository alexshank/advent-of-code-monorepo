# read input data
with open('./data/data-1.txt','r') as data_file:
     data = data_file.readlines() 

# convert all data elements to ints
for i in range(len(data)):
    data[i] = int(data[i])

# check all combinations of sums
for i in range(len(data)):
    for j in range(i+1, len(data)):
        for k in range(j+1, len(data)):
            if(data[i] + data[j] + data[k] == 2020):
                print('Answer: ' + str(data[i] * data[j] * data[k]))