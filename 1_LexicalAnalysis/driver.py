import sys
from Lexer import *

if __name__ == "__main__":
    """
    This file must not be modified.
    The file contains the code that tests the implementation of the lexical analyzer.
    """

    lexer = Lexer(sys.stdin.read())
    for token in lexer.tokens():
        print(f"{token.kind.name}")