#!/usr/local/bin/python3

import sys, os, os.path, subprocess, shutil

def test_all_from(program, path):
    for vm_file in get_all_vms(path):
        test_vm(program, vm_file)

def delocalized(filename):
    return filename[2:] if filename[:2] == './' else filename

def test_vm(program, vm_file):
    vm_copy = delocalized(shutil.copy(vm_file, '.'))
    print("VM file:", vm_copy)
    prefix = vm_file[:-3]
    test_copy = delocalized(shutil.copy(prefix + '.tst', '.'))
    print("test_copy:", test_copy)
    shutil.copy(prefix + '.cmp', '.')
    #callList = program.split() + [vm_copy]
    #subprocess.call(callList)
    subprocess.run(program + [vm_copy])
    subprocess.run(['CPUEmulator.sh', test_copy])

def get_all_vms(path):
    result = []
    for file in os.listdir(path):
        full_file = path + "/" + file
        if os.path.isdir(full_file):
            result.extend(get_all_vms(full_file))
        elif file[-3:] == ".vm":
            result.append(full_file)
    return result

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        test_all_from(sys.argv[1:], '/Users/gabriel/courses/230/f16/grading/projects/07')
    else:
        print("Usage: grade230_VM_1.py program (e.g. grade230_VM_1.py python3 vm.py)")

