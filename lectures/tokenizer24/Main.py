from Tokenizer import *

def main():
    t = Tokenizer('example.txt', ['let'])
    while t.has_more_tokens():
        t.advance()
        if t.get_token_type() == INT:
            print(t.get_int())
        else:
            print(t.token)

main()
