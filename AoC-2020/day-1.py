# read input data
with open('./data/data-1.txt','r') as data_file:
     data = data_file.readlines() 

# check all combinations of sums
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if(int(data[i]) + int(data[j]) == 2020):
            print('Answer: ' + str(int(data[i]) * int(data[j])))