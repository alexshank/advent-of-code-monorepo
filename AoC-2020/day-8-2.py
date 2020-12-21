# read input data
with open('./data/data-8.txt','r') as data_file:
     data = data_file.readlines()

# represents little kid's game device
class GameBoy:
    # constructor
    def __init__(self, data):
        # object properties
        self.instructions = []
        self.values = []
        self.accumulator = 0
        self.program_length = 0
        self.executed_indices = set()

        # initialize properties using input data
        for line in data:
            self.instructions.append(line[:3])
            self.values.append(int(line[4:-1]))
        self.program_length = len(self.instructions)
    
    # utility function for swapping jmp with nop and vice versa
    def swapInstructions(self, address):
        if self.instructions[address] == 'nop':
            self.instructions[address] = 'jmp'
        elif self.instructions[address] == 'jmp':
            self.instructions[address] = 'nop'

    # Part II fix nop or jmp error
    def fixProgram(self):
        for i in range(self.program_length):
            if self.instructions[i] == 'nop' or self.instructions[i] == 'jmp':      
                self.swapInstructions(i)
                success = self.executeProgram()
                if success:
                    print('Answer: ' + str(self.accumulator))
                    break
                else:
                    self.swapInstructions(i)
                
    # execute an entire program
    def executeProgram(self) -> bool:
        self.accumulator = 0
        self.executed_indices = set()
        pc = 0
        previous_set_len = 0
        while 0 <= pc < len(self.instructions):
            # catch instruction before it's executed twice
            previous_set_len = len(self.executed_indices)
            self.executed_indices.add(pc)
            if len(self.executed_indices) - previous_set_len == 0:
                break

            # execute instruction and update program counter
            pc = self.executeInstruction(pc)
        
        # return program success status
        return pc == self.program_length

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
gb.fixProgram()