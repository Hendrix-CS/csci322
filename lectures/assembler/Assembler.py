# Assembler!

# To start, just a program to read in a .asm file and write ot back out
# to a .hack file

import sys

instructions = {
    'ML': '100',
    'MR': '101',
    'ER': '000',
    'WR': '001',
    'JC': '010',
    'JS': '011'
}

asm_file_name = sys.argv[1]
asm_file = open(asm_file_name, 'r')

base_name = asm_file_name.split('.')[0]
hack_file_name = base_name + '.hack'

hack_file = open(hack_file_name, 'w')

# First pass: strip out comments,
# keep track of labels, save instructions
# in a list.
instr_list = []
cur_instr = 0
# Symbol table maps names to their memory location
symbol_table = {}

for line in asm_file:
    line = line.split('//')[0].strip()
    if line != '':
        if line[0] == '(':
            symbol_table[line[1:-1]] = cur_instr
        else:
            instr_list.append(line)
            cur_instr += 1

# Pass 2: go through instructions and translate
# to machine code

for instr in instr_list:
    if instr[0] == '@':
        if instr[1:].isdigit():
            n = int(instr[1:])
        else:
            n = symbol_table[instr[1:]]

        hack_file.write(f'{n:06b}\n')
    else:
        hack_file.write('111' + instructions[instr] + '\n')

asm_file.close()
hack_file.close()
