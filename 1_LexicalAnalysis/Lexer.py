import sys
import enum


class Token:
    """
    This class contains the definition of Tokens. A token has two fields: its
    text and its kind. The "kind" of a token is a constant that identifies it
    uniquely. See the TokenType to know the possible identifiers (if you want).
    You don't need to change this class.
    """
    def __init__(self, tokenText, tokenKind):
        # The token's actual text. Used for identifiers, strings, and numbers.
        self.text = tokenText
        # The TokenType that this token is classified as.
        self.kind = tokenKind


class TokenType(enum.Enum):
    """
    These are the possible tokens. You don't need to change this class at all.
    """
    EOF = -1  # End of file
    NLN = 0   # New line
    WSP = 1   # White Space
    COM = 2   # Comment
    STR = 3   # Strings
    TRU = 4   # The constant true
    FLS = 5   # The constant false
    INT = 6   # Number (integers)
    BIN = 7   # Number (binary)
    OCT = 8   # Number (octal)
    HEX = 9   # Number (hexadecimal)
    EQL = 201
    ADD = 202
    SUB = 203
    MUL = 204
    DIV = 205
    LEQ = 206
    LTH = 207
    NEG = 208
    NOT = 209
    LPR = 210
    RPR = 211


class Lexer:
    
    def __init__(self, source):
        """
        The constructor of the lexer. It receives the string that shall be
        scanned.
        TODO: You will need to implement this method.
        """
        pass

    def tokens(self):
        """
        This method is a token generator: it converts the string encapsulated
        into this object into a sequence of Tokens. Examples:

        >>> l = Lexer("10")
        >>> [tk.kind.name for tk in l.tokens()]
        ['INT']

        >>> l = Lexer("01")
        >>> [tk.kind.name for tk in l.tokens()]
        ['OCT']

        >>> l = Lexer("0b1")
        >>> [tk.kind.name for tk in l.tokens()]
        ['BIN']

        >>> l = Lexer("0B1")
        >>> [tk.kind.name for tk in l.tokens()]
        ['BIN']

        >>> l = Lexer("0x1")
        >>> [tk.kind.name for tk in l.tokens()]
        ['HEX']

        >>> l = Lexer("0X1")
        >>> [tk.kind.name for tk in l.tokens()]
        ['HEX']

        >>> l = Lexer("0X1 + 0xA + 0XABCDEF + 0xA0B1C2D3E4F5")
        >>> [tk.kind.name for tk in l.tokens()]
        ['HEX', 'ADD', 'HEX', 'ADD', 'HEX', 'ADD', 'HEX']

        >>> l = Lexer("0b1 + 0xA + 0B01010101 + 0xA0B1C2D3E4F5")
        >>> [tk.kind.name for tk in l.tokens()]
        ['BIN', 'ADD', 'HEX', 'ADD', 'BIN', 'ADD', 'HEX']

        >>> l = Lexer('1 * 2 - 3')
        >>> [tk.kind.name for tk in l.tokens()]
        ['INT', 'MUL', 'INT', 'SUB', 'INT']

        >>> l = Lexer('1 * 2 - 3 -- alkdjf adkjf dlkjf \\n')
        >>> [tk.kind.name for tk in l.tokens()]
        ['INT', 'MUL', 'INT', 'SUB', 'INT', 'COM']

        >>> l = Lexer('1 * 2 - 3 -- alkdjf adkjf dlkjf \\n0x23 + 012')
        >>> [tk.kind.name for tk in l.tokens()]
        ['INT', 'MUL', 'INT', 'SUB', 'INT', 'COM', 'HEX', 'ADD', 'OCT']
        """
        token = self.getToken()
        while token.kind != TokenType.EOF:
            if token.kind != TokenType.WSP and token.kind != TokenType.NLN:
                yield token
            token = self.getToken()

    def getToken(self):
        """
        Return the next token.
        TODO: Implement this method!
        """
        token = None
        return token