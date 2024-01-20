#!/usr/local/bin/python3

import sys
from grade230_VM_1 import get_all_vms, test_all_from

base = '/Users/gabriel/courses/230/f16/grading/projects/'

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        test_all_from(sys.argv[1:], base + '07')
        test_all_from(sys.argv[1:], base + '08/ProgramFlow')
        test_all_from(sys.argv[1:], base + '08/FunctionCalls/SimpleFunction')
    else:
        print("Usage: grade230_VM_2a.py program")

