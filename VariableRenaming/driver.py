import sys
from Expression import *
from Visitor import *
from Lexer import Lexer
from Parser import Parser
import Asm as AsmModule

def rename_variables(exp):
    """
    This function invokes the variable renamer. It should be used before
    beginning the code generation phase.    
    """
    ren = RenameVisitor()
    exp.accept(ren, {})
    return exp

if __name__ == "__main__":
    """
    This file must not be modified.
    The file contains the code that tests the implementation of the parser.
    """
    text = sys.stdin.read()
    lexer = Lexer(text)
    parser = Parser(lexer.tokens())
    exp = rename_variables(parser.parse())
    prog = AsmModule.Program({}, [])
    gen = GenVisitor()
    var_answer = exp.accept(gen, prog)
    prog.eval()
    print(f"{prog.get_val(var_answer)}")