import sys
from Expression import *
from Visitor import *
from Lexer import Lexer
from Parser import Parser
import Asm as AsmModule
from Optimizer import *


def rename_variables(exp):
    """
    This function invokes the variable renamer. It should be used before
    beginning the code generation phase. 
    """
    ren = RenameVisitor()
    exp.accept(ren, {})
    return exp


def perform_register_allocation(prog, dump=False):
    """
    This function invokes the register allocator on the program. If you want to
    debug your allocation, feel free to use dump == True.
    """
    o = RegAllocator(prog)
    if dump:
        print("Before RA: ---------------")
        prog.print_insts()
    o.optimize()
    if dump:
        print("After RA: ---------------")
        prog.print_insts()
    return o


if __name__ == "__main__":
    """
    his file must not be modified.
    The file contains the code that tests the implementation of the parser.
    """
    text = sys.stdin.read()
    lexer = Lexer(text)
    parser = Parser(lexer.tokens())
    exp = rename_variables(parser.parse())
    prog = AsmModule.Program(1000, {}, [])
    gen = GenVisitor()
    var_answer = exp.accept(gen, prog)
    opt = perform_register_allocation(prog, False)
    prog.reset_env()
    prog.eval()
    print(f"Answer: {opt.get_val(var_answer)}")