#!/usr/local/bin/python3

import sys, shutil, subprocess, os

def test_all_from(program, path, target_suffix):
    for project in os.listdir(path):
        target = './' + project
        if not os.path.isdir(target):
            shutil.copytree(path + '/' + project, target)
        for file in os.listdir(target):
            if file.endswith('.xml'):
                os.remove(target + os.sep + file)
            
        for file in os.listdir(target):
            if file.endswith('.jack'):
                copied = target + '/' + file
                generated = copied.replace('.jack', '2' + target_suffix)
                #generated = copied.replace('.jack', '-copy' + target_suffix)
                original = path + '/' + project + '/' + file
                reference = original.replace('.jack', target_suffix)
                print("Checking: ", copied)
                print("Reference:", reference)
                print("Generated:", generated)
                subprocess.run(program + [copied])
                diff = subprocess.run(['/Users/gabriel/courses/230/nand2tetris/tools/TextComparer.sh', reference, generated])
                if diff.returncode: print("Error code:", diff.returncode)
                print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: grade230_[Tokenizer|Parser].py execute-student-prog")
        sys.exit(1)
    else:
        suffix = ".xml"
        if sys.argv[0].endswith("Tokenizer.py"):
            suffix = 'T' + suffix
        test_all_from(sys.argv[1:],
                      '/Users/gabriel/courses/230/nand2tetris/projects/10',
                      suffix)

