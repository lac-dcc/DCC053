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

class EvalVisitor(Visitor):
    """
    The EvalVisitor class evaluates logical and arithmetic expressions. The
    result of evaluating an expression is the value of that expression. The
    inherited attribute propagated throughout visits is the environment that
    associates the names of variables with values.
    
    Notice that this implementation must perform type verification. If some
    verification fail, then it invokes sys.exit with the correct error
    message. We expect two different messages:
    
    1. sys.exit("Type error")
    2. sys.exit("Def error")

    Examples:
    >>> e0 = Let('v', Add(Num(40), Num(2)), Mul(Var('v'), Var('v')))
    >>> e1 = Not(Eql(e0, Num(1764)))
    >>> ev = EvalVisitor()
    >>> e1.accept(ev, {})
    False

    >>> e0 = Let('v', Add(Num(40), Num(2)), Sub(Var('v'), Num(2)))
    >>> e1 = Lth(e0, Var('x'))
    >>> ev = EvalVisitor()
    >>> e1.accept(ev, {'x': 41})
    True
    """
    def visit_var(self, exp, env):
        # TODO: Implement this method!
        raise NotImplementedError

    def visit_bln(self, exp, env):
        # TODO: Implement this method!
        raise NotImplementedError

    def visit_num(self, exp, env):
        # TODO: Implement this method!
        raise NotImplementedError

    def visit_eql(self, exp, env):
        # TODO: Implement this method!
        raise NotImplementedError

    def visit_and(self, exp, env):
        # TODO: Implement this method!
        raise NotImplementedError

    def visit_or(self, exp, env):
        # TODO: Implement this method!
        raise NotImplementedError

    def visit_add(self, exp, env):
        # TODO: Implement this method!
        raise NotImplementedError

    def visit_sub(self, exp, env):
        # TODO: Implement this method!
        raise NotImplementedError

    def visit_mul(self, exp, env):
        # TODO: Implement this method!
        raise NotImplementedError

    def visit_div(self, exp, env):
        # TODO: Implement this method!
        raise NotImplementedError

    def visit_leq(self, exp, env):
        # TODO: Implement this method!
        raise NotImplementedError

    def visit_lth(self, exp, env):
        # TODO: Implement this method!
        raise NotImplementedError

    def visit_neg(self, exp, env):
        # TODO: Implement this method!
        raise NotImplementedError

    def visit_not(self, exp, env):
        # TODO: Implement this method!
        raise NotImplementedError

    def visit_let(self, exp, env):
        # TODO: Implement this method!
        raise NotImplementedError
        
    def visit_ifThenElse(self, exp, env):
        # TODO: Implement this method!
        raise NotImplementedError