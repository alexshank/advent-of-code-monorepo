from math import sin, cos, pi

# read input data
with open('./data/data-12.txt','r') as data_file:
	data = data_file.readlines()

# object representing your ferry
class Ferry:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.waypoint_x = 10	# relative to self.x
		self.waypoint_y = 1		# relative to self.y

	# move in a direction, turn, or go forward
	def takeAction(self, instr, value):
		if instr == 'N': 	self.waypoint_y += value
		elif instr == 'S':	self.waypoint_y -= value
		elif instr == 'E':	self.waypoint_x += value
		elif instr == 'W':	self.waypoint_x -= value
		elif instr == 'L' or instr == 'R':
			# using rotation matrix (angle is counterclockwise)
			theta = value * pi / 180
			if instr == 'R': theta *= -1
			cosine, sine = int(cos(theta)), int(sin(theta))
			temp_x = self.waypoint_x*cosine - self.waypoint_y*sine
			self.waypoint_y = self.waypoint_x*sine + self.waypoint_y*cosine
			self.waypoint_x = temp_x
		elif instr == 'F':
			self.x += self.waypoint_x * value
			self.y += self.waypoint_y * value

# parse instructions
ferry = Ferry()
actions = [(line[0], int(line[1:-1])) for line in data]
for instr, value in actions:
	ferry.takeAction(instr, value)

# print puzzle answer
print('Answer: ' + str(abs(ferry.x) + abs(ferry.y)))
