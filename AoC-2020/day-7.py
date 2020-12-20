import copy

# read input data
with open('./data/data-7.txt','r') as data_file:
#with open('./data/data-7-test.txt','r') as data_file:
     data = data_file.readlines()

# parse input into parent and children colors
def parseInput(line):
    line = line[:-2]    # remove newline character and period
    [color, back] = line.split(' bags contain ')
    pairs = back.split(', ')
    children = {}
    for pair in pairs:
        # handle no children case
        if pair == 'no other bags':
            break

        # handle at least one child case
        count = int(pair[0])
        suffix_index = -4
        if count > 1: suffix_index = -5 # bag versus bags
        child_color = pair[2:suffix_index]  # ignore count and ' bags' at end of color
        children[child_color] = count
    
    # package results
    return [color, children]

# create class for to handle tree relationship of bags
class Bag:
    # constructor
    def __init__(self, color, count, children=[]):
        self.color = color
        self.count = count
        self.children = []
        if len(children) > 0:
            for [k, v] in children.items():
                child_color = k
                child_count = v
                self.children.append(Bag(child_color, child_count))
        
    # determine if a bag color is a child of this bag
    # (i.e. this bag is an ancestor of the given bag)
    def contains(self, color, color_set, topBag=True):
        # outermost bag cannot contain itself
        result = False
        if self.color == color and topBag == False:
            result = True
        elif self.color != color and len(self.children) > 0:
            for child in self.children:
                result = result or child.contains(color, color_set, False)

        # update color set and return results
        if topBag == True and result == True:
            color_set.add(self.color)
        return result

    # Part II solution
    def innerBagCount(self):
        # shiny gold node
        if len(self.children) > 0:
            result = 0
            for child in self.children:
                result = result + child.count
                result = result + child.count * child.innerBagCount()
            return result
        # leaf node (empty bag)
        else:
            return 0

    def printChildren(self):
        if len(self.children) > 0:
            for child in self.children:
                print('\t' + child.color + ' - ' + str(child.count))
                child.printChildren()

# parse all input data into Bag objects
bags = []
for line in data:
    [color, children] = parseInput(line)
    bags.append(Bag(color, -1, children))

# connect children (bag[i]) and parent bags (bags[j])
for i in range(len(bags)):
    match_color = bags[i].color
    for j in range(len(bags)):
        for x in range(len(bags[j].children)):
            if bags[j].children[x].color == match_color:
                child_bag = bags[i]
                # if child already has count set, create copy
                if child_bag.count != -1:
                    child_bag = copy.copy(child_bag)
                    bags.append(child_bag)
                child_bag.count = bags[j].children[x].count
                bags[j].children[x] = child_bag 

# count ancestors of shiny gold tree node
shiny_gold_index = -1
color_set = set()
for i in range(len(bags)):
    bags[i].contains('shiny gold', color_set)
    if bags[i].color == 'shiny gold': shiny_gold_index = i

# print puzzle answer
print('Answer: ' + str(len(color_set)))
print('Answer: ' + str(bags[shiny_gold_index].innerBagCount()))