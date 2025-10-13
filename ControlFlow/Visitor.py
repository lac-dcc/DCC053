import sys
from abc import ABC, abstractmethod
from Expression import *
import Asm as AsmModule


class Visitor(ABC):
    """
    The visitor pattern consists of two abstract classes: the Expression and the
    Visitor. The Expression class defines on method: 'accept(visitor, args)'.
    This method takes in an implementation of a visitor, and the arguments that
    are passed from expression to expression. The Visitor class defines one
    specific method for each subclass of Expression. Each instance of such a
    subclasse will invoke the right visiting method.
    """
    @abstractmethod
    def visit_var(self, exp, arg):
        pass

    @abstractmethod
    def visit_bln(self, exp, arg):
        pass

    @abstractmethod
    def visit_num(self, exp, arg):
        pass

    @abstractmethod
    def visit_eql(self, exp, arg):
        pass

    @abstractmethod
    def visit_and(self, exp, arg):
        pass

    @abstractmethod
    def visit_or(self, exp, arg):
        pass

    @abstractmethod
    def visit_add(self, exp, arg):
        pass

    @abstractmethod
    def visit_sub(self, exp, arg):
        pass

    @abstractmethod
    def visit_mul(self, exp, arg):
        pass

    @abstractmethod
    def visit_div(self, exp, arg):
        pass

    @abstractmethod
    def visit_leq(self, exp, arg):
        pass

    @abstractmethod
    def visit_lth(self, exp, arg):
        pass

    @abstractmethod
    def visit_neg(self, exp, arg):
        pass

    @abstractmethod
    def visit_not(self, exp, arg):
        pass

    @abstractmethod
    def visit_let(self, exp, arg):
        pass

    @abstractmethod
    def visit_ifThenElse(self, exp, arg):
        pass

class GenVisitor(Visitor):
    """
    The GenVisitor class compiles arithmetic expressions into a low-level
    language.
    """

    def __init__(self):
        self.next_var_counter = 0

    def next_var_name(self):
        """
        You can use this method to get fresh variable names.
        """
        self.next_var_counter += 1
        return f"v{self.next_var_counter}"

    def visit_var(self, exp, prog):
        """
        Usage:
            >>> e = Var('x')
            >>> p = AsmModule.Program({"x":1}, [])
            >>> g = GenVisitor()
            >>> v = e.accept(g, p)
            >>> p.eval()
            >>> p.get_val(v)
            1
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_bln(self, exp, prog):
        """
        Usage:
            >>> e = Bln(True)
            >>> p = AsmModule.Program({}, [])
            >>> g = GenVisitor()
            >>> v = e.accept(g, p)
            >>> p.eval()
            >>> p.get_val(v)
            1

            >>> e = Bln(False)
            >>> p = AsmModule.Program({}, [])
            >>> g = GenVisitor()
            >>> v = e.accept(g, p)
            >>> p.eval()
            >>> p.get_val(v)
            0
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_num(self, exp, prog):
        """
        Usage:
            >>> e = Num(13)
            >>> p = AsmModule.Program({}, [])
            >>> g = GenVisitor()
            >>> v = e.accept(g, p)
            >>> p.eval()
            >>> p.get_val(v)
            13
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_eql(self, exp, prog):
        """
        >>> e = Eql(Num(13), Num(13))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        1

        >>> e = Eql(Num(13), Num(10))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        0

        >>> e = Eql(Num(-1), Num(1))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        0
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_and(self, exp, prog):
        """
        >>> e = And(Bln(True), Bln(True))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        1

        >>> e = And(Bln(False), Bln(True))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        0

        >>> e = And(Bln(True), Bln(False))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        0

        >>> e = And(Bln(False), Bln(False))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        0

        >>> e = And(Bln(False), Div(Num(3), Num(0)))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        0
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_or(self, exp, prog):
        """
        >>> e = Or(Bln(True), Bln(True))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        1

        >>> e = Or(Bln(False), Bln(True))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        1

        >>> e = Or(Bln(True), Bln(False))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        1

        >>> e = Or(Bln(False), Bln(False))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        0

        >>> e = Or(Bln(True), Div(Num(3), Num(0)))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        1
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_add(self, exp, prog):
        """
        >>> e = Add(Num(13), Num(-13))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        0

        >>> e = Add(Num(13), Num(10))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        23
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_sub(self, exp, prog):
        """
        >>> e = Sub(Num(13), Num(-13))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        26

        >>> e = Sub(Num(13), Num(10))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        3
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_mul(self, exp, prog):
        """
        >>> e = Mul(Num(13), Num(2))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        26

        >>> e = Mul(Num(13), Num(10))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        130
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_div(self, exp, prog):
        """
        >>> e = Div(Num(13), Num(2))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        6

        >>> e = Div(Num(13), Num(10))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        1
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_leq(self, exp, prog):
        """
        >>> e = Leq(Num(3), Num(2))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        0

        >>> e = Leq(Num(3), Num(3))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        1

        >>> e = Leq(Num(2), Num(3))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        1

        >>> e = Leq(Num(-3), Num(-2))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        1

        >>> e = Leq(Num(-3), Num(-3))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        1

        >>> e = Leq(Num(-2), Num(-3))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        0
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_lth(self, exp, prog):
        """
        >>> e = Lth(Num(3), Num(2))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        0

        >>> e = Lth(Num(3), Num(3))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        0

        >>> e = Lth(Num(2), Num(3))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        1
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_neg(self, exp, prog):
        """
        >>> e = Neg(Num(3))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        -3

        >>> e = Neg(Num(0))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        0

        >>> e = Neg(Num(-3))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        3
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_not(self, exp, prog):
        """
        >>> e = Not(Bln(True))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        0

        >>> e = Not(Bln(False))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        1

        >>> e = Not(Num(0))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        1

        >>> e = Not(Num(-2))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        0

        >>> e = Not(Num(2))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        0
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_let(self, exp, prog):
        """
        Usage:
            >>> e = Let('v', Not(Bln(False)), Var('v'))
            >>> p = AsmModule.Program({}, [])
            >>> g = GenVisitor()
            >>> v = e.accept(g, p)
            >>> p.eval()
            >>> p.get_val(v)
            1

            >>> e = Let('v', Num(2), Add(Var('v'), Num(3)))
            >>> p = AsmModule.Program({}, [])
            >>> g = GenVisitor()
            >>> v = e.accept(g, p)
            >>> p.eval()
            >>> p.get_val(v)
            5

            >>> e0 = Let('x', Num(2), Add(Var('x'), Num(3)))
            >>> e1 = Let('y', e0, Mul(Var('y'), Num(10)))
            >>> p = AsmModule.Program({}, [])
            >>> g = GenVisitor()
            >>> v = e1.accept(g, p)
            >>> p.eval()
            >>> p.get_val(v)
            50
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_ifThenElse(self, exp, prog):
        """
        >>> e = IfThenElse(Bln(True), Num(3), Num(5))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        3

        >>> e = IfThenElse(Bln(False), Num(3), Num(5))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        5

        >>> e = IfThenElse(And(Bln(True), Bln(True)), Num(3), Num(5))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        3

        >>> e0 = Mul(Num(2), Add(Num(3), Num(4)))
        >>> e1 = IfThenElse(And(Bln(True), Bln(False)), Num(3), e0)
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e1.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        14

        >>> e0 = Div(Num(2), Num(0))
        >>> e1 = IfThenElse(Bln(True), Num(3), e0)
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e1.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        3

        >>> e0 = Div(Num(2), Num(0))
        >>> e1 = IfThenElse(Bln(False), e0, Num(3))
        >>> p = AsmModule.Program({}, [])
        >>> g = GenVisitor()
        >>> v = e1.accept(g, p)
        >>> p.eval()
        >>> p.get_val(v)
        3
        """
        # TODO: Implement this method.
        raise NotImplementedError


class RenameVisitor(ABC):
    """
    This visitor traverses the AST of a program, renaming variables to ensure
    that they all have different names.

    Usage:
        >>> e0 = Let('x', Num(2), Add(Var('x'), Num(3)))
        >>> e1 = Let('x', e0, Mul(Var('x'), Num(10)))
        >>> e0.identifier == e1.identifier
        True

        >>> e0 = Let('x', Num(2), Add(Var('x'), Num(3)))
        >>> e1 = Let('x', e0, Mul(Var('x'), Num(10)))
        >>> r = RenameVisitor()
        >>> e1.accept(r, {})
        >>> e0.identifier == e1.identifier
        False

        >>> x0 = Var('x')
        >>> x1 = Var('x')
        >>> e0 = Let('x', Num(2), Add(x0, Num(3)))
        >>> e1 = Let('x', e0, Mul(x1, Num(10)))
        >>> x0.identifier == x1.identifier
        True

        >>> x0 = Var('x')
        >>> x1 = Var('x')
        >>> e0 = Let('x', Num(2), Add(x0, Num(3)))
        >>> e1 = Let('x', e0, Mul(x1, Num(10)))
        >>> r = RenameVisitor()
        >>> e1.accept(r, {})
        >>> x0.identifier == x1.identifier
        False
    """

    def __init__(self):
        # TODO: implement something here.
        pass

    def visit_var(self, exp, name_map):
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_bln(self, exp, name_map):
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_num(self, exp, name_map):
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_eql(self, exp, name_map):
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_and(self, exp, name_map):
        """
        Example:
            >>> y0 = Var('x')
            >>> y1 = Var('x')
            >>> x0 = And(Lth(y0, Num(2)), Leq(Num(2), y1))
            >>> x1 = Var('x')
            >>> e0 = Let('x', Num(2), Add(x0, Num(3)))
            >>> e1 = Let('x', e0, Mul(x1, Num(10)))
            >>> r = RenameVisitor()
            >>> e1.accept(r, {})
            >>> y0.identifier == y1.identifier
            True

            >>> y0 = Var('x')
            >>> y1 = Var('x')
            >>> x0 = And(Lth(y0, Num(2)), Leq(Num(2), y1))
            >>> x1 = Var('x')
            >>> e0 = Let('x', Num(2), Add(x0, Num(3)))
            >>> e1 = Let('x', e0, Mul(x1, Num(10)))
            >>> r = RenameVisitor()
            >>> e1.accept(r, {})
            >>> y0.identifier == x1.identifier
            False
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_or(self, exp, name_map):
        """
        Example:
            >>> y0 = Var('x')
            >>> y1 = Var('x')
            >>> x0 = Or(Lth(y0, Num(2)), Leq(Num(2), y1))
            >>> x1 = Var('x')
            >>> e0 = Let('x', Num(2), Add(x0, Num(3)))
            >>> e1 = Let('x', e0, Mul(x1, Num(10)))
            >>> r = RenameVisitor()
            >>> e1.accept(r, {})
            >>> y0.identifier == y1.identifier
            True

            >>> y0 = Var('x')
            >>> y1 = Var('x')
            >>> x0 = Or(Lth(y0, Num(2)), Leq(Num(2), y1))
            >>> x1 = Var('x')
            >>> e0 = Let('x', Num(2), Add(x0, Num(3)))
            >>> e1 = Let('x', e0, Mul(x1, Num(10)))
            >>> r = RenameVisitor()
            >>> e1.accept(r, {})
            >>> y0.identifier == x1.identifier
            False
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_add(self, exp, name_map):
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_sub(self, exp, name_map):
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_mul(self, exp, name_map):
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_div(self, exp, name_map):
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_leq(self, exp, name_map):
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_lth(self, exp, name_map):
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_neg(self, exp, name_map):
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_not(self, exp, name_map):
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_ifThenElse(self, exp, name_map):
        """
        Example:
            >>> x0 = Var('x')
            >>> x1 = Var('x')
            >>> e0 = IfThenElse(Lth(x0, x1), Num(1), Num(2))
            >>> e1 = Let('x', Num(3), e0)
            >>> r = RenameVisitor()
            >>> e1.accept(r, {})
            >>> x0.identifier == x1.identifier
            True

            >>> x0 = Var('x')
            >>> x1 = Var('x')
            >>> e0 = IfThenElse(Lth(x0, x1), Num(1), Num(2))
            >>> e1 = Let('x', Num(3), e0)
            >>> e2 = Let('x', e1, Num(3))
            >>> r = RenameVisitor()
            >>> e1.accept(r, {})
            >>> e2.identifier != x1.identifier == e1.identifier
            True
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_let(self, exp, name_map):
        # TODO: Implement this method.
        raise NotImplementedError