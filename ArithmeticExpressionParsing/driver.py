import sys
from Expression import *
from Lexer import Lexer
from Parser import Parser

if __name__ == "__main__":
    """
    This file must not be modified.
    The file contains the code that tests the implementation of the parser.
    """
    lexer = Lexer(sys.stdin.read())
    parser = Parser(lexer.tokens())
    exp = parser.parse()
    print(f"Value is {exp.eval()}")