import sys
from Unifier import *
from Lexer import Lexer
from Parser import Parser

def print_types(type_names):
    """
    This method runs the type inference engine, and prints the type of
    variables 'x', 'y' and 'z', if they exist in the test case.
    """
    print(f"Type(v): {type_names.setdefault('v', type(None)).__name__}")
    print(f"Type(w): {type_names.setdefault('w', type(None)).__name__}")
    print(f"Type(x): {type_names.setdefault('x', type(None)).__name__}")
    print(f"Type(y): {type_names.setdefault('y', type(None)).__name__}")
    print(f"Type(z): {type_names.setdefault('z', type(None)).__name__}")

if __name__ == "__main__":
    """
    This file must not be modified.
    The file contains the code that tests the implementation of the parser.
    """
    text = sys.stdin.read()
    lexer = Lexer(text)
    parser = Parser(lexer.tokens())
    expression = parser.parse()
    print_types(infer_types(expression))