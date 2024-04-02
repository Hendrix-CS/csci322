from Tokenizer import *
from VMWriter import *
import sys

class Compiler:
    def __init__(self, input_file_name, output_file_name):
        self.tokenizer = Tokenizer(input_file_name,[])
        self.w = VMWriter(output_file_name)

    def expect(self, tok):
        t = self.tokenizer.next()
        if not (t.token_type == SYMBOL and t.value == tok):
            print(f"Error! Expected {tok} but got {t.value}")
            sys.exit(1)

    def compile_num(self, t):
        self.w.write_push(CONSTANT, t.value)

    def do_op(self, op):
        if op == '+':
            self.w.write_raw('add')
        elif op == '-':
            self.w.write_raw('sub')
        elif op == '*':
            self.w.write_call('Math.multiply', 2)
        else:
            print(f"Unexpected operator '{op}'!")
            sys.exit(1)

    def compile_expr(self):
        t = self.tokenizer.next()

        if t.token_type == INT:
            self.compile_num(t)
        elif t.token_type == SYMBOL and t.value == '(':
            op = self.compile_op()

            self.compile_expr()

            while self.tokenizer.peek().value != ')':
                self.compile_expr()
                self.do_op(op.value)

            self.expect(')')
        else:
            print("Error!! Expecting an expr, but saw something other than number or (")
            sys.exit(1)

    def compile_op(self) -> Token:
        t = self.tokenizer.next()
        if t.token_type == SYMBOL:
            return t
        else:
            print(f"Error, expecting an operator, but got {t.value}.")
            sys.exit(1)

def main():
    filename = sys.argv[1]
    out_file = filename.split('.')[0] + '.vm'
    lc = Compiler(filename, out_file)
    lc.compile_expr()

main()
