#!/usr/local/bin/python3

import sys, os, os.path, subprocess, shutil

base = '/Users/gabriel/courses/230/nand2tetris/projects/08/FunctionCalls/'
targets = ['NestedCall','FibonacciElement','StaticsTest']

def test_vm(program, vm_file, tst_file, cmp_file):
    subprocess.run(['cp', '-r', vm_file, '.'])
    vm_copy = vm_file.split('/')[-1]
    print("VM:", vm_copy)
    subprocess.run(program + [vm_copy])
    asm = find('.', vm_copy + '.asm')
    if asm:
        asm_where = '/'.join(asm.split('/')[:-1])
        shutil.copy(cmp_file, asm_where)
        subprocess.run(["CPUEmulator.sh", shutil.copy(tst_file, asm_where)])
    else:
        print("asm file not found")

def find(base, name):
    for file in os.listdir(base):
        full = base + '/' + file
        if os.path.isdir(full):
            found = find(full, name)
            if found: return found
        elif file == name:
            return full

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        subprocess.run(['rm', '-rf'] + targets)
        program = sys.argv[1:]
        vms = [(base+f, base+f+'/'+f+".tst", base+f+os.sep+f+".cmp")
               for f in targets]
        for (vm_file, tst_file, cmp_file) in vms:
            test_vm(program, vm_file, tst_file, cmp_file)
    else:
        print("Usage: grade230_VM_2b.py program")
