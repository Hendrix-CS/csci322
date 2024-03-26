INT = 0
KEYWORD = 1
IDENTIFIER = 2

def is_ident_char(c):
    return c.isalnum() or c == '_'

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

        # Make sure we skip past any spaces + comments
        # at the very beginning of the file.
        self.eat_whitespace()

    # Skip past any spaces + comments.
    # Convention: we will always call this function
    # right after reading in each token, so we will
    # be ready to read the next token.
    def eat_whitespace(self):
        done = False
        while not done and self.pos < len(self.text):
            if self.text[self.pos].isspace():
                self.pos += 1
            else:
                done = True

            # Still need to handle comments!

    def has_more_tokens(self) -> bool:
        return self.pos < len(self.text)

    # Advance to the next token.
    # Precondition: should only be called
    #   if has_more_tokens() returns true.
    # Set self.token_type and self.token
    def advance(self):
        if self.text[self.pos].isdigit():
            self.token_type = INT
            self.token = ''

            while self.pos < len(self.text) and self.text[self.pos].isdigit():
                self.token += self.text[self.pos]
                self.pos += 1

        elif is_ident_char(self.text[self.pos]):
            self.token = ''

            while self.pos < len(self.text) and is_ident_char(self.text[self.pos]):
                self.token += self.text[self.pos]
                self.pos += 1

            if self.token in self.keywords:
                self.token_type = KEYWORD
            else:
                self.token_type = IDENTIFIER

        # Eat up whitespace in preparation for the next token
        self.eat_whitespace()

    def get_token_type(self):
        return self.token_type

    # Should only be called when token_type == INT
    def get_int(self):
        return int(self.token)
