from Tokenizer import *
import sys

class Compiler:
    def __init__(self, input_file_name):
        self.tokenizer = Tokenizer(input_file_name,[])
        self.indent = 0

    def print_indented(self, thing):
        print(f'{self.indent * " "}{thing}')

    def expect(self, tok):
        t = self.tokenizer.next()
        if not (t.token_type == SYMBOL and t.value == tok):
            print(f"Error! Expected {tok} but got {t.value}")
            sys.exit(1)

    def compile_expr(self):
        t = self.tokenizer.next()

        if t.token_type == INT:
            self.print_indented(t.value)
        elif t.token_type == SYMBOL and t.value == '(':
            self.compile_op()

            self.indent += 2
            self.compile_expr()
            self.compile_expr()
            self.indent -= 2

            self.expect(')')
        else:
            print("Error!! Expecting an expr, but saw something other than number or (")
            sys.exit(1)

    def compile_op(self):
        t = self.tokenizer.next()
        if t.token_type == SYMBOL:
            self.print_indented(t.value)
        else:
            print(f"Error, expecting an operator, but got {t.value}.")
            sys.exit(1)

def main():
    lc = Compiler('error.lisp')
    lc.compile_expr()

main()
