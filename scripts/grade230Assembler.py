#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import sys
import shutil
import subprocess

if len(sys.argv) < 2:
    print("Usage: grade230Assembler.py execute-student-prog (in quotation marks)")
    sys.exit(1)

basedir = '/Users/gabriel/courses/230/f15/nand2tetris/projects/06/'

targets = ['add/Add', 'max/Max', 'max/MaxL', 'pong/Pong',
           'pong/PongL', 'rect/Rect', 'rect/RectL']

for target in targets:
    print("Trying", target)
    fullTarget = target + '.asm'
    assembleTarget = fullTarget.split('/')[1]
    refTarget = target + '.hack1'
    shutil.copy(basedir + fullTarget, '.')
    shutil.copy(basedir + refTarget, '.')
    refTarget = refTarget.split('/')[1]
    callList = sys.argv[1].split() + [assembleTarget]
    print("About to call subprocess: ", callList)
    subprocess.call(callList)
    print("subprocess called")
    subprocess.call(['diff', refTarget[:-1], refTarget])
    print("diff completed")
