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
    def visit_mod(self, exp, arg):
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
    def visit_fun(self, exp, arg):
        pass

    @abstractmethod
    def visit_app(self, exp, arg):
        pass


class Function:
    """
    This is the class that represents functions. This class lets us distinguish
    the three types that now exist in the language: numbers, booleans and
    functions. Notice that the evaluation of an expression can now be a
    function. For instance:

        >>> f = Fn('v', Mul(Var('v'), Var('v')))
        >>> ev = EvalVisitor()
        >>> fval = f.accept(ev, {})
        >>> type(fval)
        <class 'Visitor.Function'>
    """

    def __init__(self, formal, body, env):
        self.formal = formal
        self.body = body
        self.env = env

    def __str__(self):
        return f"Fn({self.formal})"


class RecFunction(Function):
    """
    This is the class that represents named functions. The key different between
    named and anonymous functions is exactly the "name" :)

        >>> f = Fun('f', 'v', Mul(Var('v'), Var('v')))
        >>> ev = EvalVisitor()
        >>> fval = f.accept(ev, {})
        >>> type(fval)
        <class 'Visitor.RecFunction'>
    """

    def __init__(self, name, formal, body, env):
        super().__init__(formal, body, env)
        self.name = name

    def __str__(self):
        return f"Fun {self.name}({self.formal})"


class EvalVisitor(Visitor):
    """
    The EvalVisitor class evaluates logical and arithmetic expressions. The
    result of evaluating an expression is the value of that expression. The
    inherited attribute propagated throughout visits is the environment that
    associates the names of variables with values.

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

    >>> e0 = Fn('v', Mul(Var('v'), Var('v')))
    >>> ev = EvalVisitor()
    >>> print(e0.accept(ev, {}))
    Fn(v)

    >>> e0 = Fn('v', Mul(Var('v'), Var('v')))
    >>> e1 = Add(Num(3), Num(4))
    >>> e2 = App(e0, e1)
    >>> ev = EvalVisitor()
    >>> print(e2.accept(ev, {}))
    49

    >>> e0 = Fun('f', 'v', Mul(Var('v'), Var('v')))
    >>> ev = EvalVisitor()
    >>> print(e0.accept(ev, {}))
    Fun f(v)

    >>> e0 = Fun('f', 'v', Mul(Var('v'), Var('v')))
    >>> e1 = Add(Num(3), Num(4))
    >>> e2 = App(e0, e1)
    >>> ev = EvalVisitor()
    >>> print(e2.accept(ev, {}))
    49
    """

    def visit_var(self, exp, env):
        if exp.identifier in env:
            return env[exp.identifier]
        else:
            sys.exit("Def error")

    def visit_bln(self, exp, env):
        return exp.bln

    def visit_num(self, exp, env):
        return exp.num

    def visit_eql(self, exp, env):
        val_left = exp.left.accept(self, env)
        val_right = exp.right.accept(self, env)
        if type(val_left) == type(val_right):
            return val_left == val_right
        else:
            sys.exit("Type error")

    def visit_and(self, exp, env):
        # TODO: Implement this method.
        raise NotImplementedException

    def visit_or(self, exp, env):
        # TODO: Implement this method.
        raise NotImplementedException

    def visit_add(self, exp, env):
        # TODO: Implement this method.
        raise NotImplementedException

    def visit_sub(self, exp, env):
        # TODO: Implement this method.
        raise NotImplementedException

    def visit_mul(self, exp, env):
        # TODO: Implement this method.
        raise NotImplementedException

    def visit_div(self, exp, env):
        # TODO: Implement this method.
        raise NotImplementedException

    def visit_mod(self, exp, env):
        # TODO: Implement this method.
        raise NotImplementedException

    def visit_leq(self, exp, env):
        # TODO: Implement this method.
        raise NotImplementedException

    def visit_lth(self, exp, env):
        # TODO: Implement this method.
        raise NotImplementedException

    def visit_neg(self, exp, env):
        # TODO: Implement this method.
        raise NotImplementedException

    def visit_not(self, exp, env):
        # TODO: Implement this method.
        raise NotImplementedException

    def visit_let(self, exp, env):
        # TODO: Implement this method.
        raise NotImplementedException

    def visit_ifThenElse(self, exp, env):
        # TODO: Implement this method.
        raise NotImplementedException
        
    def visit_fn(self, exp, env):
        """
        The evaluation of a function is the function itself. Remember: in our
        language, functions are values as well. So, now we have four kinds of
        values: numbers, booleans, anonymous functions and named functions.
        """
        return Function(exp.formal, exp.body, env)

    def visit_fun(self, exp, env):
        """
        The evaluation of a named function returns a value that is the function
        itself. However, we use a different type of value: RecFunction. In this
        way, we have access to the name of the named function (and that's why
        they are called named functions :).
        """
        return RecFunction(exp.name, exp.formal, exp.body, env)

    def visit_app(self, exp, env):
        """
        The application of function to actual parameter must contain two cases:
        1. An anonymous function is applied: (fn x => x + 1) 2
        2. A named function is applied: f 2, where f is fun f a = a + a
        The only difference between these two cases is that in the second we
        must augment the environment with the name of the named function.

        Example:
        >>> f = Fun('f', 'v', Mul(Var('v'), Var('v')))
        >>> e0 = Let('f', f, App(Var('f'), Num(2)))
        >>> ev = EvalVisitor()
        >>> e0.accept(ev, {})
        4
        """
        # TODO: Implement this method.
        raise NotImplementedException