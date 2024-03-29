# NOTE!!! This is an old version.  Much better to have tokenizer
# create list of all tokens up front (using a Token class to create
# token objects) then implement peek() and next() functions.  See
# compiler24/Tokenizer.py.

# Arbitrary constants to represent token types

KEYWORD = 0
INT = 1
SYMBOL = 2
IDENTIFIER = 3

# Arbitrary constants to represent keywords

class Tokenizer:
    def __init__(self, text, keywords):
        self.pos = 0     # current position in text
        self.text = text
        self.keywords = keywords  # allowed keywords

        self.eat_whitespace()    # get ready for first token

    def eat_whitespace(self):
        done = False
        while not done and self.pos < len(self.text):
            if self.text[self.pos].isspace():
                self.pos += 1
            elif self.pos < len(self.text) - 1 and self.text[self.pos:self.pos + 2] == '//':
                self.pos = self.pos + 2
                while self.pos < len(self.text) and self.text[self.pos] != '\n':
                    self.pos += 1
            else:
                done = True

    def has_more_tokens(self):
        return self.pos < len(self.text)

    # Read the next token + consume trailing whitespace
    # Set variables self.token_type and self.token
    #
    # Should only be called if has_more_tokens is true
    def advance(self):
        # Check for INT tokens first
        if self.text[self.pos].isdigit():
            self.token = ''
            while self.pos < len(self.text) and self.text[self.pos].isdigit():
                self.token += self.text[self.pos]
                self.pos += 1
            self.token_type = INT

        # Now check for identifiers
        elif self.text[self.pos].isalpha() or self.text[self.pos] == '_':
            self.token = ''
            while self.pos < len(self.text) and isidchar(self.text[self.pos]):
                self.token += self.text[self.pos]
                self.pos += 1
            if self.token in self.keywords:
                self.token_type = KEYWORD
            else:
                self.token_type = IDENTIFIER

        else:
            self.token_type = SYMBOL
            self.token = self.text[self.pos]
            self.pos += 1

        self.eat_whitespace()

    def get_token_type(self):
        return self.token_type

    # Should only be called if token_type is INT
    def int_val(self):
        return int(self.token)

    def identifier(self):
        return self.token

    def keyword(self):
        return self.token

    def symbol(self):
        return self.token

def isidchar(c):
    return c.isalnum() or c == '_'

if __name__ == "__main__":
    t = Tokenizer("let x5 = y + 99;\n  let z = (y + 2) * (x5-7);", ["let"])
    print("<tokens>")
    while t.has_more_tokens():
        t.advance()
        if t.get_token_type() == INT:
            print(f"<int> {t.int_val()} </int>")
        else:
            print(t.token)
    print("</tokens>")
