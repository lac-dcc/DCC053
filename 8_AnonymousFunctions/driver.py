import sys
from Expression import *
from Visitor import *
from Lexer import Lexer
from Parser import Parser

if __name__ == "__main__":
    """
    This file must not be modified.
    The file contains the code that tests the implementation of the parser.
    """
    text = sys.stdin.read()
    lexer = Lexer(text)
    parser = Parser(lexer.tokens())
    exp = parser.parse()
    visitor = EvalVisitor()
    print(f"{exp.accept(visitor, {})}")