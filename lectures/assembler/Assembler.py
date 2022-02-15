#!/bin/python3
# Assembler!

# TM CPU instructions:

# ML   100
# MR   101
# JC   010
# JS   011
# ER   000
# WR   001

import sys

instrs = {
    'ML': '100',
    'MR': '101',
    'JC': '010',
    'JS': '011',
    'ER': '000',
    'WR': '001'
}

input_file_name = sys.argv[1]

# Find name of output file
file_base = input_file_name.split('.')[0]
output_file_name = file_base + '.hack'

# Open input & output files
input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')

# Process each line

for line in input_file:
    line = line.split('//')[0].strip()
    if line != '':
        output_file.write('111' + instrs[line.strip()] + '\n')

input_file.close()
output_file.close()
