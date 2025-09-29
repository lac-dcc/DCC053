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
    (option, rest) = text.split(maxsplit=1)
    lexer = Lexer(rest)
    parser = Parser(lexer.tokens())
    exp = parser.parse()
    if option == 'eval':
        visitor = EvalVisitor()
        print(f"Value is {exp.accept(visitor, {})}")
    elif option == 'usedef':
        visitor = UseDefVisitor()
        print(f"Are there undefs? {len(exp.accept(visitor, set())) > 0}")
    elif option == 'safe_eval':
        safe_eval(exp)
    else:
        sys.exit(f"Invalid option = {option}")