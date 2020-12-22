# read input data
with open('./data/data-11.txt','r') as data_file:
     data = data_file.readlines() 

# create 2D array from data (represents matrix of seat locations)
data = [list(line[:-1]) for line in data]
last_r = len(data) - 1
last_c = len(data[0]) - 1

# different adjacent seats to check around each seat 
MAIN_OFFSETS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] 
TOP_OFFSETS = [(0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] 
BOTTOM_OFFSETS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1)] 
LEFT_OFFSETS = [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, 1)] 
RIGHT_OFFSETS = [(-1, -1), (-1, 0), (0, -1), (1, -1), (1, 0)] 
TOP_LEFT_OFFSETS = [(0, 1), (1, 0), (1, 1)] 
BOTTOM_LEFT_OFFSETS = [(-1, 0), (-1, 1), (0, 1)] 
TOP_RIGHT_OFFSETS = [(0, -1), (1, -1), (1, 0)] 
BOTTOM_RIGHT_OFFSETS = [(-1, -1), (-1, 0), (0, -1)] 

# Part II
# function to check for occupied seat in given direction
def occupiedInLine(r, c, del_r, del_c):
     x = r + del_r
     y = c + del_c
     while True:
          # look further away
          if data[x][y] == '.':
               x = x + del_r
               y = y + del_c 
               if x < 0 or x > last_r or y < 0 or y > last_c: return False
          else:
               return data[x][y] == '#'

# check if an empty/occupied seat should be toggled
def checkSeatChange(r, c, offsets) -> bool:
     # floor seats never change
     if data[r][c] == '.': return False
     # checks for empty seat that should become occupied
     elif data[r][c] == 'L':
          for del_r, del_c in offsets:
                    # Part I: if data[r + del_r][c + del_c] == '#':
                    if occupiedInLine(r, c, del_r, del_c):
                         return False
          return True
     # checks for occupied seat that should become empty
     else:
          occuppied_count = 0
          for del_r, del_c in offsets:
                    # Part I: if data[r + del_r][c + del_c] == '#':
                    if occupiedInLine(r, c, del_r, del_c):
                         occuppied_count += 1
                         if occuppied_count == 5: return True    # changed from 4 to 5 for Part II
          return False 

# check sections of seating that have different adjacent seats (offsets)
def getSeatChangesInRange(r_range, c_range, offsets):
     changes = []
     for r in r_range:
          for c in c_range:
               if checkSeatChange(r, c, offsets): changes.append((r, c))
     return changes

# check each seat location for needed toggles
def getSeatChanges() -> list:
     # locations with 9 adjecent squares
     changes = []
     changes.extend(getSeatChangesInRange(range(1, last_r), range(1, last_c), MAIN_OFFSETS))

     # locations on left and right borders
     changes.extend(getSeatChangesInRange(range(1, last_r), [0], LEFT_OFFSETS))
     changes.extend(getSeatChangesInRange(range(1, last_r), [last_c], RIGHT_OFFSETS))

     # locations on top and bottom borders
     changes.extend(getSeatChangesInRange([0], range(1, last_c), TOP_OFFSETS))
     changes.extend(getSeatChangesInRange([last_r], range(1, last_c), BOTTOM_OFFSETS))

     # four corners
     changes.extend(getSeatChangesInRange([0], [0], TOP_LEFT_OFFSETS))
     changes.extend(getSeatChangesInRange([0], [last_c], TOP_RIGHT_OFFSETS))
     changes.extend(getSeatChangesInRange([last_r], [0], BOTTOM_LEFT_OFFSETS))
     changes.extend(getSeatChangesInRange([last_r], [last_c], BOTTOM_RIGHT_OFFSETS))
     return changes

# continue updating seats until seats stop toggling
settled = False
while settled == False:
     changes = getSeatChanges()
     # seats are no longer changing
     if len(changes) == 0: settled = True
     # update seats with needed toggles
     else:
          for r, c in changes: data[r][c] = '#' if data[r][c] == 'L' else 'L'

# print puzzle answer
occupied = sum(map(lambda x: x.count('#'), data))
print('Answer: ' + str(occupied))
