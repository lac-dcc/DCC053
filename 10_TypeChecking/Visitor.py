import sys
from abc import ABC, abstractmethod
from Expression import *


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

    @abstractmethod
    def visit_fn(self, exp, arg):
        pass

    @abstractmethod
    def visit_app(self, exp, arg):
        pass


class ArrowType:
    """
    This is the class that represents function types. A function type is just
    that: the type of a function. Function types are also called "arrow types",
    because they tend to be represented as 't0 -> t1'. Thus, an arrow type
    has two parts: the head type (t0) and the tail type (t1).

    Usage:
        >>> t = ArrowType(type(1), type(True))
        >>> t.hd == type(1) and t.tl == type(True)
        True

        >>> t = ArrowType(type(1), type(True))
        >>> str(t)
        "<class 'int'> -> <class 'bool'>"
    """

    def __init__(self, tp_formal, tp_body):
        self.hd = tp_formal
        self.tl = tp_body

    def __eq__(self, other):
        """
        Two arrow types are equal if their head and tail are equal.
        Example:
            >>> t0 = ArrowType(type(1), ArrowType(type(1), type(1)))
            >>> t1 = ArrowType(type(1), ArrowType(type(1), type(1)))
            >>> t0 == t1
            True
        """
        if isinstance(other, ArrowType):
            return self.hd == other.hd and self.tl == other.tl
        else:
            return False

    def __repr__(self):
        if isinstance(self.hd, ArrowType):
            hd_str = f"( {str(self.hd)} )"
        else:
            hd_str = str(self.hd)
        if isinstance(self.tl, ArrowType):
            tl_str = f"( {str(self.tl)} )"
        else:
            tl_str = str(self.tl)
        return f"{hd_str} -> {tl_str}"


class TypeCheckVisitor(Visitor):
    """
    The TypeCheckVisitor class evaluates logical and arithmetic expressions. The
    result of evaluating an expression is the value of that expression. The
    inherited attribute propagated throughout visits is the environment that
    associates the names of variables with values.
    """

    def visit_var(self, exp, env):
        """
        Usage:
            >>> e = Var('t')
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, {'t':type(1)})
            <class 'int'>

            >>> e = Var('t')
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, {'t':ArrowType(type(1), type(True))})
            <class 'int'> -> <class 'bool'>
        """
        if exp.identifier in env:
            return env[exp.identifier]
        else:
            sys.exit("Def error")

    def visit_bln(self, exp, env):
        """
        Usage:
            >>> e = Bln(True)
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, None)
            <class 'bool'>
        """
        return type(exp.bln)

    def visit_num(self, exp, env):
        """
        Usage:
            >>> e = Num(1)
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, None)
            <class 'int'>
        """
        return type(exp.num)

    def visit_eql(self, exp, env): # Implemented for you :)
        """
        Usage:
            >>> e = Eql(Num(1), Num(2))
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, None)
            <class 'bool'>
        """
        if exp.left.accept(self, env) == exp.right.accept(self, env):
            return type(True)
        else:
            sys.exit("Type error")

    def visit_and(self, exp, env):
        """
        Usage:
            >>> e = And(Bln(True), Bln(False))
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, None)
            <class 'bool'>
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_or(self, exp, env):
        """
        Usage:
            >>> e = Or(Bln(True), Bln(False))
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, None)
            <class 'bool'>
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_add(self, exp, env):
        """
        Usage:
            >>> e = Add(Num(1), Num(2))
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, None)
            <class 'int'>
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_sub(self, exp, env):
        """
        Usage:
            >>> e = Sub(Num(1), Num(2))
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, None)
            <class 'int'>
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_mul(self, exp, env):
        """
        Usage:
            >>> e = Mul(Num(1), Num(2))
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, None)
            <class 'int'>
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_div(self, exp, env):
        """
        Usage:
            >>> e = Div(Num(1), Num(0))
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, None)
            <class 'int'>
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_leq(self, exp, env):
        """
        Usage:
            >>> e = Leq(Num(1), Num(0))
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, None)
            <class 'bool'>
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_lth(self, exp, env):
        """
        Usage:
            >>> e = Lth(Num(1), Num(0))
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, None)
            <class 'bool'>
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_neg(self, exp, env):
        """
        Usage:
            >>> e = Neg(Num(1))
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, None)
            <class 'int'>
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_not(self, exp, env):
        """
        Usage:
            >>> e = Not(Bln(False))
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, None)
            <class 'bool'>
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_ifThenElse(self, exp, env):
        """
        Usage:
            >>> e0 = Lth(Num(1), Num(0))
            >>> e = IfThenElse(e0, Bln(True), e0)
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, {})
            <class 'bool'>

            >>> e0 = Lth(Num(1), Num(0))
            >>> e = IfThenElse(e0, Var('v'), Var('w'))
            >>> ev = TypeCheckVisitor()
            >>> tp0 = ArrowType(type(1), type(2))
            >>> tp1 = ArrowType(type(3), type(4))
            >>> e.accept(ev, {'v':tp0, 'w':tp1})
            <class 'int'> -> <class 'int'>
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_let(self, exp, env):
        """
        Usage:
            >>> e = Let('v', type(True), Not(Bln(False)), Var('v'))
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, {})
            <class 'bool'>

            >>> e = Let('v', type(1), Num(2), Add(Var('v'), Num(3)))
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, {})
            <class 'int'>
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_fn(self, exp, env):
        """
        Usage:
            >>> e = Fn('v', type(True), Var('v'))
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, {})
            <class 'bool'> -> <class 'bool'>

            >>> e = Fn('v', type(1), Add(Var('v'), Num(3)))
            >>> ev = TypeCheckVisitor()
            >>> e.accept(ev, {})
            <class 'int'> -> <class 'int'>

            >>> e0 = Fn('y', type(1), Add(Var('y'), Var('x')))
            >>> e1 = Fn('x', type(1), e0)
            >>> ev = TypeCheckVisitor()
            >>> e1.accept(ev, {})
            <class 'int'> -> ( <class 'int'> -> <class 'int'> )
        """
        # TODO: Implement this method.
        raise NotImplementedError

    def visit_app(self, exp, env):
        """
        Usage:
            >>> e0 = Fn('v', type(1), Add(Var('v'), Num(3)))
            >>> e1 = App(e0, Num(1))
            >>> ev = TypeCheckVisitor()
            >>> e1.accept(ev, {})
            <class 'int'>

            >>> e0 = Fn('y', type(1), Add(Var('y'), Var('x')))
            >>> e1 = Fn('x', type(1), e0)
            >>> e2 = App(e1, Num(1))
            >>> ev = TypeCheckVisitor()
            >>> e2.accept(ev, {})
            <class 'int'> -> <class 'int'>
        """
        # TODO: Implement this method.
        raise NotImplementedError