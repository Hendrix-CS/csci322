import os
import sys

def main():

    # argument can be either a .vm file, or a directory with multiple .vm files.
    vmcode = sys.argv[1]
    outfilename = vmcode.split('.')[0] + ".hack"
    outfile = open(outfilename, 'w')

    # Generate bootstrap code if needed
    generate_bootstrap(outfile)

    if os.path.isdir(vmcode):
        # If it is a directory, translate all the .vm files inside it
        for f in os.listdir(vmcode):
            if f ends with .vm:
                translate_vm(os.path.join(vmcode, f), outfile)
    else:
        # Else just translate a single .vm file
        translate_vm(vmcode, outfile)

def translate_vm(filename, outfile):
    # Translate VM code in filename and output assembly to outfile
