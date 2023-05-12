import tokens as token

class Token:

    def __init__(self, type: str, literal: str = None) -> any:
        # Define the type and literal of each token
        self.type = type
        self.literal = literal

    def __str__(self) -> str:
         # Define how to represent each token as a string
        if self.literal:
            return f'Type {self.type} : Literal {self.literal}'
        return f'Type {self.type}'




'''
'Tokenizer' is the main class that performs the tokenization. It takes a string input as a parameter, which is the text to tokenize. It has several methods:

__init__: Initializes the object with the input text and sets the initial positions of the cursor and read_cursor.
read_char: Reads the next character from the input text and updates the cursor and read_cursor positions.
next_token: Reads the next token from the input text and returns a Token object.
read_identifier: Reads an identifier (e.g., a variable or function name) from the input text and returns it as a string.
read_number: Reads a number (integer) from the input text and returns it as a string.
consume_whitespace: Skips any whitespace characters (e.g., spaces, tabs, newlines) until a non-whitespace character is found.

'''
class Tokenizer:
    def __init__(self, input: str) -> any:


        #                         (book refernce page 13)
        #          input string
        #          position int // current position in input (points to current char)
        #          read_Position -> read_cursor int // current reading position in input (after current char)
        #          ch byte // current char under examination

        # Initialize the input, cursor, read_cursor and ch variables
        self.input: str = input  # input text
        # current position in input (points to current character)
        self.cursor: int = 0
        # current reading position in input (after current character)
        self.read_cursor: int = 0
        self.ch = ''  # current character under examination, need to see how to get byte or rune type in python3

        '''
            Let’s use readChar in our New() function so our *Lexer is in a fully working state before anyone calls NextToken(), 
            with l.ch, l.position and l.readPosition already initialized:                (quote from book)
        '''

        self.read_char()
        '''
       The utilization of two pointers in our current approach is necessitated by our need to gain a wider perspective of 
            the input data beyond the current character we are examining. It is noteworthy that the read_cursor pointer will 
            consistently point to the subsequent character of the input that we are yet to examine, while the cursor pointer will
            always point to the character in the input that corresponds to the ch byte that we are currently processing.
        
        !!! read_cursor will always point to "next" character of input !!!
        
        '''

    '''
    The main objective of utilizing the read_char method is to obtain the subsequent character from the input and subsequently 
        move ahead in our position within the input. This method plays a crucial role in ensuring that we can access each character 
        of the input sequentially while maintaining the correct order of characters. By calling the read_char method, we are able 
        to progress through the input data and retrieve each character in turn, enabling us to perform various operations on the 
        data as required.

                                 !!!  supports only UTF-8,  !!!
    '''



# A first helper method called readChar() should make the usage of these fields easier to under- stand:  (quote from book)
    def read_char(self) -> any:

         # Read the next character in the input and update the cursor and read_cursor accordingly
        if self.read_cursor >= len(self.input):
            self.ch = 0
        else:
            self.ch = self.input[self.read_cursor]
        self.cursor = self.read_cursor
        self.read_cursor += 1

    def next_token(self) -> Token:
         # Determine the next token based on the current character
        tok: Token = Token(token.EOF, "")
        self.consume_whitespace()

        if self.ch == "=":
            tok = Token(token.ASSIGN)
        elif self.ch == '+':
            tok = Token(token.PLUS)
        elif self.ch == ':':
            tok = Token(token.COLON)
        elif self.ch == ';':
            tok = Token(token.SEMICOLON)
        elif self.ch == ',':
            tok = Token(token.COMMA)
        elif self.ch == '.':  # extend for fields (amm, cap, in, out)
            tok = Token(token.DOT)
        elif self.ch == '(':
            tok = Token(token.LPAREN)
        elif self.ch == ')':
            tok = Token(token.RPAREN)
        elif self.ch == '{':
            tok = Token(token.LBRACE)
        elif self.ch == '}':
            tok = Token(token.RBRACE)
        elif self.ch == 0:
            tok = Token(token.EOF)
        else:
            if is_letter(self.ch):
                tok.literal = self.read_identifier()
                tok.type = token.lookup_ident(tok.literal)
                return Token(tok.type, tok.literal)
            if is_digit(self.ch) and self.ch != '0':
                tok.literal = self.read_number()
                tok.type = token.INT
                return Token(token.INT, tok.literal)

            tok = Token(token.ILLEGAL, self.ch)

        self.read_char()

        return tok

    def read_identifier(self) -> str:
        # Read an identifier from the input
        cursor: int = self.cursor

        while is_letter(self.ch) or is_digit(self.ch):
            self.read_char()

        return self.input[cursor: self.cursor]

    def read_number(self) -> str:
         # Read a number from the input
        cursor: int = self.cursor

        while is_digit(self.ch):
            self.read_char()

        return self.input[cursor: self.cursor]

    def consume_whitespace(self) -> None:
         # Consume whitespace characters from the input
        while self.ch == ' ' or self.ch == '\t' or self.ch == '\n' or self.ch == '\r':
            self.read_char()

def is_letter(ch: str) -> bool:
     # Determine if a character is a letter or underscore
    return 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or ch == '_'


def is_digit(ch: str) -> bool:
     # Determine if a character is a digit
    return '0' <= ch <= '9'
