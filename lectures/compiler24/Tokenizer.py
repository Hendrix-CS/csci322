INT = 0
KEYWORD = 1
IDENTIFIER = 2
SYMBOL = 3

def is_ident_char(c):
    return c.isalnum() or c == '_'

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type

        # The type of self.value will depend on the token_type
        # e.g. if token_type == INT, then self.value will
        # be an int, etc.
        self.value = value

class Tokenizer:

    def __init__(self, input_file_name, keywords):
        with open(input_file_name) as input_file:
            # read entire input file and save it
            # in a variable
            self.text = input_file.read()

        self.keywords = keywords

        # Keep track of our current position
        # in the text
        self.pos = 0

        # List of all tokens
        self.tokens = []
        # Index of the current token
        self.cur_token = 0

        self.process_tokens()

    # Read all the tokens into a list
    def process_tokens(self):

        # Make sure we skip past any spaces + comments
        # at the very beginning of the file.
        self.eat_whitespace()

        while self.pos < len(self.text):
            self.tokens.append(self.advance())

    # Skip past any spaces + comments.
    # Convention: we will always call this function
    # right after reading in each token, so we will
    # be ready to read the next token.
    def eat_whitespace(self):
        done = False
        while not done and self.pos < len(self.text):
            if self.text[self.pos].isspace():
                self.pos += 1
            elif self.pos < len(self.text) - 1 and self.text[self.pos:self.pos+2] == '//':
                self.pos += 2  # skip past //
                while self.pos < len(self.text) and self.text[self.pos] != '\n':
                    self.pos += 1
                self.pos += 1   # skip past the \n
            else:
                done = True


    # Advance to the next token.
    # Precondition: should only be called
    #   if has_more_tokens() returns true.
    # Set self.token_type and self.token
    def advance(self) -> Token:
        if self.text[self.pos].isdigit():
            digits = ''

            while self.pos < len(self.text) and self.text[self.pos].isdigit():
                digits += self.text[self.pos]
                self.pos += 1

            token = Token(INT, int(digits))

        elif is_ident_char(self.text[self.pos]):
            token_chars = ''

            while self.pos < len(self.text) and is_ident_char(self.text[self.pos]):
                token_chars += self.text[self.pos]
                self.pos += 1

            if token_chars in self.keywords:
                token_type = KEYWORD
            else:
                token_type = IDENTIFIER

            token = Token(token_type, token_chars)

        else:   # must be a symbol
            token = Token(SYMBOL, self.text[self.pos])
            self.pos += 1

        # Eat up whitespace in preparation for the next token
        self.eat_whitespace()

        return token

    def has_more_tokens(self) -> bool:
        return self.cur_token < len(self.tokens)

    def next(self) -> Token:
        token = self.tokens[self.cur_token]
        self.cur_token += 1
        return token

    def peek(self) -> Token:
        return self.tokens[self.cur_token]
