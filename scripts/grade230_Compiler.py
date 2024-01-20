#!/usr/local/bin/python3

import sys, shutil, subprocess, os

def test_all_from(program, path):
    for project in os.listdir(path):
        target = './' + project
        if not os.path.isdir(target):
            shutil.copytree(path + '/' + project, target)
            
        for file in os.listdir(target):
            if file.endswith('.jack'):
                copied = target + '/' + file
                print("Compiling", copied)
                subprocess.run(program + [copied])
                print("Complete")
                print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: grade230_Compiler.py execute-student-prog")
        sys.exit(1)
    else:
        test_all_from(sys.argv[1:],
                      '/Users/gabriel/courses/230/nand2tetris/projects/11')

