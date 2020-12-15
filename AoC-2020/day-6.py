# read input data
with open('./data/data-6.txt','r') as data_file:
     data = data_file.readlines()

# get groups of people from input data
groups = []
group = []
i = 0
for line in data:
    if line == '\n':
        groups.append(group)
        group = []
    else:
        group.append(line[:-1])

# count questions that everyone in a group answered "yes" to
total_sum = 0
for group in groups:
    question_count = 0
    # if only one person in group, count all their questions
    if len(group) == 1:
        question_count = len(group[0])
    else:
        # first person defines questions to test
        for question in group[0]:
            all_contain = True
            for person in group[1:]:
                if question not in person:
                    all_contain = False
                    break
            if all_contain: question_count = question_count + 1

    # add group question count to running sum
    total_sum = total_sum + question_count

# print answer
print('Answer: ' + str(total_sum))
