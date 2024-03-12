#!/bin/env python3
import os
import shutil
import subprocess

project_dir = "/home/brent/teaching/322/"
semester = '24G'
grading_dir = project_dir + semester + '/grading/'
n2t_dir     = project_dir + 'pristine/nand2tetris/'
testing_dir = n2t_dir + 'projects/'
tools_dir   = n2t_dir + 'tools/'

exe_ext = ".sh"

# If restrictions is empty, return true.  Otherwise, check whether the
# path has some subpart which is an element of 'restrictions'.
# i.e. we can use this to restrict to only looking at certain paths.
def meets_restrictions(path, restrictions):
    return not restrictions or any(r in path for r in restrictions)

# Recursively check all files in base_dir with the given suffix which
# match one of the given patterns in 'restrictions', by calling
# check_func on them.  But exclude any files under a directory named 'graded'.
def file_checker(base_dir, suffix, restrictions, check_func):
    if os.path.isdir(base_dir):
        for filename in os.listdir(base_dir):
            file_path = base_dir + os.path.sep + filename
            if os.path.isdir(file_path):
                if filename != 'graded':
                    file_checker(file_path, suffix, restrictions, check_func)
            elif filename[-len(suffix):] == suffix and meets_restrictions(file_path, restrictions):
                check_func(file_path)

# Recursively list all the files in base_dir with a given suffix.  For
# testing.
def show_files(base_dir, suffix):
    file_checker(base_dir, suffix, [], lambda path: print(f"found {path}"))

# Grade all the .hdl files in the given base_dir by calling HardwareSimulator on them
def grade_hdl(base_dir, test_dir, expected, restrictions):
    grade_tst(base_dir, test_dir, expected, "HardwareSimulator", ".hdl", restrictions)

# Grade all the .asm files in the given base_dir by first running an Assembler on them,
# then calling the CPUEmulator.
def grade_asm(base_dir, test_dir, expected, restrictions):
    file_checker(base_dir, ".asm", restrictions, assemble)
    grade_tst(base_dir, test_dir, expected, "CPUEmulator", ".asm", restrictions)

# Run the assembler on a file.
def assemble(filename):
    subprocess.call([tools_dir + os.path.sep + "Assembler" + exe_ext, filename])

# Grade .asm files by running the CPUEmulator directly.
def grade_asm_direct(base_dir, test_dir, expected, restrictions):
    grade_tst(base_dir, test_dir, expected, "CPUEmulator", ".asm", restrictions)

# Grade some files using corresponding .tst files.
def grade_tst(base_dir, test_dir, expected, test_script_name, target_suffix, restrictions):
    # ensure_present(base_dir, target_suffix, expected
    file_checker(base_dir, target_suffix, restrictions, lambda path: check_tst(expected, test_dir, path, test_script_name))

def check_tst(expected, test_dir, file_to_test, test_script_name):
    where = os.path.dirname(file_to_test)
    prefix = os.path.basename(file_to_test)[:-4]
    if prefix in expected or prefix.capitalize() in expected:
        if type(expected) == dict:
            testers = [test for test in expected[prefix] if test[-4:] == ".tst"]
            to_copy = expected[prefix] + [test.replace('.tst', '.cmp') for test in testers]
        else:
            testers = [prefix + '.tst']
            to_copy = testers + [prefix + '.cmp']
        for copy in to_copy:
            shutil.copy(test_dir + os.path.sep + copy, where)
        for tester in testers:
            print(f"Testing {prefix} with {tester} in {where}")
            subprocess.call([tools_dir + test_script_name + exe_ext, where + os.path.sep + tester])


def grade_project_1(restrictions):
    grade_hdl(f"{grading_dir}/01", f"{testing_dir}/01",
              {"Not", "And", "Or", "Mux", "DMux", "Not16", "And16", "Or16", "Mux16", "Mux4Way16", "Mux8Way16", "DMux4Way", "DMux8Way", "Or8Way"},
              restrictions)


def grade_project_2(restrictions):
    grade_hdl(f"{grading_dir}/02", f"{testing_dir}/02",
              {"HalfAdder", "FullAdder", "Add16", "Inc16", "Or16Way", "ALU"},
              restrictions)


def grade_project_3(restrictions):
    grade_hdl(f"{grading_dir}/03", f"{testing_dir}/03/a",
              {"Bit", "Register", "RAM8", "RAM64", "PC"},
              restrictions)
    grade_hdl(f"{grading_dir}/03", f"{testing_dir}/03/b",
              {"RAM512", "RAM4K", "RAM16K"},
              restrictions)


def grade_project_4(restrictions):
    grade_asm(f"{grading_dir}/04", f"{testing_dir}/04/mult", {"Mult"}, restrictions)
    grade_asm(f"{grading_dir}/04", f"{testing_dir}/04/fill",
              {"Fill": ["FillAutomatic.tst"]}, restrictions)


def grade_project_5(restrictions):
    grade_hdl(f"{grading_dir}/05", f"{testing_dir}/05",
              {"CPU": ["CPU.tst"],
               "Computer": ["ComputerAdd.tst", "Add.hack", "ComputerMax.tst", "Max.hack", "ComputerRect.tst",
                            "Rect.hack"]},
              restrictions)

def grade_project_6(restrictions):
    testing_dir_06 = f"{testing_dir}/06"
    grading_dir_06 = f"{grading_dir}/06/tograde"
    pristine_dir = f"{project_dir}/nand2tetris/projects/06-cmp"
    tests = ["add/Add", "max/Max", "rect/Rect", "pong/Pong"]
    for dir in os.listdir(grading_dir_06):
        if os.path.isdir(dir):
            student_path = f"{grading_dir_06}/{dir}"
            if meets_restrictions(student_path, restrictions):
                print(f"Testing {student_path}...")
                copy_dirs_from(testing_dir_06, student_path)
                ok = True
                for t in tests:
                    subprocess.call([f"{student_path}/assembler", f"{student_path}/{t}.asm"])
                    ret = subprocess.call([f"diff", "-Z", f"{pristine_dir}/{t}.hack", f"{student_path}/{t}.hack"])
                    ok = ok and (ret == 0)
                print("All tests passed!" if ok else "Tests failed.")

def test_generated_asm(id, dirs, restrictions):
    vm_sub_dir = f"{grading_dir}/{id}/tograde"
    for dir in os.listdir(vm_sub_dir):
        if os.path.isdir(os.path.join(vm_sub_dir, dir)):
            student_path = vm_sub_dir + os.path.sep + dir
            print(f"Considering {student_path}...")
            if meets_restrictions(student_path, restrictions):
                print(f"Testing {student_path}...")
                copy_dirs_from(testing_dir + os.path.sep + "07", student_path)
                for d in os.listdir(student_path):
                    if d in dirs:
                        for vm_project in os.listdir(student_path + os.path.sep + d):
                            grade_asm_direct(student_path + os.path.sep + d + os.path.sep + vm_project,
                                          f"{testing_dir}/{id}/{d}/{vm_project}",
                                          {f"{vm_project}"},
                                          restrictions)


def test_generated_asm_7(restrictions):
    test_generated_asm("07", ('MemoryAccess', 'StackArithmetic'), restrictions)


def test_generated_asm_8(restrictions):
    test_generated_asm("08", {'FunctionCalls'}, restrictions)


def copy_dirs_from(src_parent, target_location):
    for file in os.listdir(src_parent):
        full_src = src_parent + os.path.sep + file
        full_destination = target_location + os.path.sep + os.path.basename(file)
        if os.path.isdir(full_src) and not os.path.exists(full_destination):
            print(f"copying {full_src} to {full_destination}")
            shutil.copytree(full_src, full_destination)


def copy_to_submissions(src_parent, target_base, target_pattern, restrictions):
    for_files_in_pattern(target_base, target_pattern, restrictions, lambda file: copy_dirs_from(src_parent, file))


def diff(target_base, target_pattern, files_to_diff, restrictions):
    for_files_in_pattern(target_base, target_pattern, restrictions, lambda file: run_diff(file, files_to_diff))


def run_diff(base_dir, diff_pattern):
    print("Checking", base_dir)
    os.chdir(base_dir)
    suffix1, suffix2, candidates = diff_pattern
    for candidate in candidates:
        print(candidate)
        subprocess.call(["TextComparer.bat", candidate + suffix1, candidate + suffix2])


def for_files_in_pattern(target_base, target_pattern, restrictions, consumer):
    for candidate in os.listdir(target_base):
        full_candidate = target_base + os.path.sep + candidate
        if target_pattern in candidate and os.path.isdir(full_candidate) and meets_restrictions(full_candidate, restrictions):
            consumer(full_candidate)


# Haven't found the right way to use this yet, if at all...
def assemble_all_in(base_dir):
    file_checker(base_dir, ".asm", [], lambda file: subprocess.call(["Assembler.bat", file]))


if __name__ == "__main__":
    reply = "continue"
    base_dir = project_dir + "submissions"
    dispatch = {"01": grade_project_1, "02": grade_project_2, "03": grade_project_3,
                "04": grade_project_4, "05": grade_project_5, "06": grade_project_6,
                "07": test_generated_asm_7, "08": test_generated_asm_8}
    diffs = {"06": (".baseline", ".hack", ["add\\Add", "max\\MaxL", "rect\\RectL", "pong\\PongL", "max\\Max", "rect\\Rect", "pong\\Pong"])}

    while reply[0] != "q":
        print("Choices:")
        print("show [file suffix] *[project id]")
        print(f"grade [{'|'.join([key for key in dispatch])}]")
        print("copy_dirs [project id]")
        print(f"diff [{'|'.join([key for key in diffs])}]")
        print("quit")
        reply = input("Enter choice:")
        pieces = reply.split()
        if pieces[0] == "show":
            if len(pieces) >= 3:
                show_files(base_dir + os.path.sep + pieces[2], pieces[1])
            else:
                show_files(base_dir, pieces[1])
        elif pieces[0] == "grade":
            if pieces[1] in dispatch:
                dispatch[pieces[1]](pieces[2:])
            else:
                print(f"Project {pieces[1]} has no grading function")
        elif pieces[0] == "copy_dirs":
            copy_to_submissions(
                project_dir + "nand2tetris" + os.path.sep + "projects" + os.path.sep + pieces[1] + os.path.sep,
                grading_dir + os.path.sep + pieces[1] + os.path.sep + "tograde",
                "", pieces[2:])
        elif pieces[0] == "diff":
            diff(grading_dir + "submissions" + os.path.sep + pieces[1], "assignsubmission_file", diffs[pieces[1]], pieces[2:])
