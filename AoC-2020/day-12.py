# read input data
with open('./data/data-12.txt','r') as data_file:
	data = data_file.readlines()

# object representing your ferry
class Ferry:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.facing = 0		# 0, 1, 2, 3 represent E, N, W, S

	# move in a direction, turn, or go forward
	def takeAction(self, instr, value):
		if instr == 'N': 	self.y += value
		elif instr == 'S':	self.y -= value
		elif instr == 'E':	self.x += value
		elif instr == 'W':	self.x -= value
		elif instr == 'L':
			self.facing += value / 90
			self.facing %= 4
		elif instr == 'R':
			self.facing -= value / 90
			self.facing %= 4
		elif instr == 'F':
			if self.facing == 0: self.x += value
			elif self.facing == 1: self.y += value
			elif self.facing == 2: self.x -= value
			elif self.facing == 3: self.y -= value
	
# parse instructions
ferry = Ferry()
actions = [(line[0], int(line[1:-1])) for line in data]
for instr, value in actions:
	ferry.takeAction(instr, value)

# print puzzle answer
print('Answer: ' + str(abs(ferry.x) + abs(ferry.y)))


