# read input data
with open('./data/data-8.txt','r') as data_file:
#with open('./data/data-7-test.txt','r') as data_file:
     data = data_file.readlines()

# represents little kid's game device
class GameBoy:
    # constructor
    def __init__(self, data):
        # object properties
        self.instructions = []
        self.values = []
        self.accumulator = 0
        self.executedIndices = set()

        # initialize properties using input data
        for line in data:
            self.instructions.append(line[:3])
            self.values.append(int(line[4:-1]))

    # execute an entire program
    def executeProgram(self):
        pc = 0
        previous_set_len = 0
        while 0 <= pc < len(self.instructions):
            # catch instruction before it's executed twice
            previous_set_len = len(self.executedIndices)
            self.executedIndices.add(pc)
            if len(self.executedIndices) - previous_set_len == 0:
                print('Answer: ' + str(self.accumulator))
                break

            # update program counter
            pc = self.executeInstruction(pc)

    # execute a single instruction (return new pc value)
    def executeInstruction(self, pc) -> int:
        instruction = self.instructions[pc]
        value = self.values[pc]

        # branch to implemented commands
        if instruction == 'nop':
            return pc + 1
        elif instruction == 'acc':
            self.accumulator += value
            return pc + 1
        elif instruction == 'jmp':
            return pc + value

# create instance of GameBoy
gb = GameBoy(data)
gb.executeProgram()