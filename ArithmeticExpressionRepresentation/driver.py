import sys
from Expression import *

if __name__ == "__main__":
    """
    This file must not be modified.
    The file contains the code that tests the implementation of the lexical analyzer.
    """
    e = eval(sys.stdin.read())
    print(f"Value is {e.eval()}")