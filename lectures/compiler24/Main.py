from Tokenizer import *

def main():
    tokenizer = Tokenizer('example.txt', ['let'])

    t = tokenizer.peek()
    print(f'{t.token_type}: {t.value}')

    while tokenizer.has_more_tokens():
        t = tokenizer.next()

        print(f'{t.token_type}: {t.value}')

main()
