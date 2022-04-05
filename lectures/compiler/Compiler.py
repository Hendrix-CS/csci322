# Compiler to translate LISP expressions into Jack VM code.
#
# e.g.  (+ 1 (* 2 3))
#
# should translate to something like
#
# push constant 1
# push constant 2
# push constant 3
# call Math.multiply 2
# add
#
# expr: num | list
# list: '(' op expr expr ')'
# op: '+' | '*'

from Tokenizer import *

import sys

ops = { '+': 'add', '*': 'call Math.multiply 2' }

class Compiler:

    def __init__(self, code):
        self.tokenizer = Tokenizer(code, [])
        self.vm_code = []
        self.compile_expr()

    def emit(self, vm):
        self.vm_code.append(vm)

    def next_token(self):
        self.tokenizer.advance()
        self.token_type = self.tokenizer.get_token_type()

    def compile_expr(self):
        # Get the next token and figure out whether we are in the num
        # case or the list case
        self.next_token()

        if self.token_type == INT:
            self.compile_num(self.tokenizer.int_val())
        elif self.token_type == SYMBOL and self.tokenizer.symbol() == '(':
            self.compile_list()
        else:
            print("Error: expected either num or '(' at start of expr")
            print(f"but got {self.tokenizer.token} instead")
            sys.exit(1)

    def compile_num(self, n):
        self.emit(f"push constant {n}")

    def compile_list(self):
        self.next_token()

        if self.token_type == SYMBOL and self.tokenizer.symbol() in ops:
            op = self.tokenizer.symbol()
            self.compile_expr()
            self.compile_expr()
            self.emit(ops[op])
            self.next_token()
        else:
            print(f"Error: unknown operator {self.token}")

    def print_vm(self):
        print('\n'.join(self.vm_code))
