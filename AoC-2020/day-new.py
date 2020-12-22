'''
Creates all the files I need for a new AoC puzzle.

Alex Shank 2020
'''
import argparse

# set up argument parser
parser = argparse.ArgumentParser(description='Creates empty files needed for an AoC puzzle')
parser.add_argument('day_number',
                    type=int,
                    help='Puzzle number from 0-25 (integer)')
args = parser.parse_args()
d = str(args.day_number)

# create day-x.py
with open('./day-' + d + '.py', 'w') as py_file:
    py_file.write('# read input data\n')
    py_file.write('with open(\'./data/data-' + d + '.txt\',\'r\') as data_file:\n')
    py_file.write('\tdata = data_file.readlines()\n')

# create file for input data
input_file = open('./data/data-' + d + '.txt', 'w')
input_file.close()

# create file for puzzle prompt
with open('./prompts/prompt-' + d + '.md', 'w') as prompt_file:
    prompt_file.write('\n')
    prompt_file.write('\n')
    prompt_file.write('---\n')
    prompt_file.write('\n')
    prompt_file.write('\n')