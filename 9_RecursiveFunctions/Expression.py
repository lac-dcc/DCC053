from abc import ABC, abstractmethod
from Visitor import *

"""
This file adds recursive functions to our language. You can follow the
semantics of these functions using the rules below, which were written in
Prolog:

eval(fn(Formal, Body), Env, fval(Formal, Body, Env)).

eval(fun(Name, Formal, Body), Env, rfun(Name, Formal, Body, Env)).

eval(apply(Function, Actual), Env, Value) :-
  eval(Function, Env, fval(Formal, Body, Nesting)),
  eval(Actual, Env, PValue),
  eval(Body, [(Formal, PValue)|Nesting], Value).

eval(applyrec(Function, Actual), Env, Value) :-
  eval(Function, Env, rfun(Name, Formal, Body, Nesting)),
  eval(Actual, Env, PValue),
  NEnv = [(Name, rfun(Name, Formal, Body, Nesting)), (Formal, PValue)|Nesting]
  eval(Body, NEnv, Value).
"""


class Expression(ABC):
    @abstractmethod
    def accept(self, visitor, arg):
        raise NotImplementedError


class Var(Expression):
    """
    This class represents expressions that are identifiers. The value of an
    indentifier is the value associated with it in the environment table.
    """

    def __init__(self, identifier):
        self.identifier = identifier

    def accept(self, visitor, arg):
        """
        Example:
        >>> e = Var('var')
        >>> ev = EvalVisitor()
        >>> e.accept(ev, {'var': 42})
        42

        >>> e = Var('v42')
        >>> ev = EvalVisitor()
        >>> e.accept(ev, {'v42': True, 'v31': 5})
        True
        """
        return visitor.visit_var(self, arg)


class Bln(Expression):
    """
    This class represents expressions that are boolean values. There are only
    two boolean values: true and false. The effect of such an expression is
    the boolean itself.
    """

    def __init__(self, bln):
        self.bln = bln

    def accept(self, visitor, arg):
        """
        Example:
        >>> e = Bln(True)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        True
        """
        return visitor.visit_bln(self, arg)


class Num(Expression):
    """
    This class represents expressions that are numbers. The effect of such
    an expression is the number itself.
    """

    def __init__(self, num):
        self.num = num

    def accept(self, visitor, arg):
        """
        Example:
        >>> e = Num(3)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        3
        """
        return visitor.visit_num(self, arg)


class BinaryExpression(Expression):
    """
    This class represents binary expressions. A binary expression has two
    sub-expressions: the left operand and the right operand.
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    @abstractmethod
    def accept(self, visitor, arg):
        raise NotImplementedError


class Eql(BinaryExpression):
    """
    This class represents the equality between two expressions. The effect
    of such an expression is True if the subexpressions are the same, or false
    otherwise.
    """

    def accept(self, visitor, arg):
        """
        Example:
        >>> n1 = Num(3)
        >>> n2 = Num(4)
        >>> e = Eql(n1, n2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        False

        >>> n1 = Num(3)
        >>> n2 = Num(3)
        >>> e = Eql(n1, n2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        True
        """
        return visitor.visit_eql(self, arg)


class Add(BinaryExpression):
    """
    This class represents addition of two expressions. The effect of such
    an expression is the addition of the two subexpression's values.
    """

    def accept(self, visitor, arg):
        """
        Example:
        >>> n1 = Num(3)
        >>> n2 = Num(4)
        >>> e = Add(n1, n2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        7
        """
        return visitor.visit_add(self, arg)


class And(BinaryExpression):
    """
    This class represents the logical disjunction of two boolean expressions.
    The evaluation of an expression of this kind is the logical AND of the two
    subexpression's values.
    """

    def accept(self, visitor, arg):
        """
        Example:
        >>> b1 = Bln(True)
        >>> b2 = Bln(False)
        >>> e = And(b1, b2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        False

        >>> b1 = Bln(True)
        >>> b2 = Bln(True)
        >>> e = And(b1, b2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        True
        """
        return visitor.visit_and(self, arg)


class Or(BinaryExpression):
    """
    This class represents the logical conjunction of two boolean expressions.
    The evaluation of an expression of this kind is the logical OR of the two
    subexpression's values.
    """

    def accept(self, visitor, arg):
        """
        Example:
        >>> b1 = Bln(True)
        >>> b2 = Bln(False)
        >>> e = Or(b1, b2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        True

        >>> b1 = Bln(False)
        >>> b2 = Bln(False)
        >>> e = Or(b1, b2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        False
        """
        return visitor.visit_or(self, arg)


class Sub(BinaryExpression):
    """
    This class represents subtraction of two expressions. The effect of such
    an expression is the subtraction of the two subexpression's values.
    """

    def accept(self, visitor, arg):
        """
        Example:
        >>> n1 = Num(3)
        >>> n2 = Num(4)
        >>> e = Sub(n1, n2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        -1
        """
        return visitor.visit_sub(self, arg)


class Mul(BinaryExpression):
    """
    This class represents multiplication of two expressions. The effect of
    such an expression is the product of the two subexpression's values.
    """

    def accept(self, visitor, arg):
        """
        Example:
        >>> n1 = Num(3)
        >>> n2 = Num(4)
        >>> e = Mul(n1, n2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        12
        """
        return visitor.visit_mul(self, arg)


class Div(BinaryExpression):
    """
    This class represents the integer division of two expressions. The
    effect of such an expression is the integer quocient of the two
    subexpression's values.
    """

    def accept(self, visitor, arg):
        """
        Example:
        >>> n1 = Num(28)
        >>> n2 = Num(4)
        >>> e = Div(n1, n2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        7

        >>> n1 = Num(22)
        >>> n2 = Num(4)
        >>> e = Div(n1, n2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        5
        """
        return visitor.visit_div(self, arg)


class Mod(BinaryExpression):
    """
    This class represents the integer modulo of two expressions. The
    effect of such an expression is the integer quocient of the two
    subexpression's values.
    """

    def accept(self, visitor, arg):
        """
        Example:
        >>> n1 = Num(28)
        >>> n2 = Num(4)
        >>> e = Mod(n1, n2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        0

        >>> n1 = Num(22)
        >>> n2 = Num(4)
        >>> e = Mod(n1, n2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        2
        """
        return visitor.visit_mod(self, arg)


class Leq(BinaryExpression):
    """
    This class represents comparison of two expressions using the
    less-than-or-equal comparator. The effect of such an expression is a
    boolean value that is true if the left operand is less than or equal the
    right operand. It is false otherwise.
    """

    def accept(self, visitor, arg):
        """
        Example:
        >>> n1 = Num(3)
        >>> n2 = Num(4)
        >>> e = Leq(n1, n2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        True

        >>> n1 = Num(3)
        >>> n2 = Num(3)
        >>> e = Leq(n1, n2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        True

        >>> n1 = Num(4)
        >>> n2 = Num(3)
        >>> e = Leq(n1, n2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        False
        """
        return visitor.visit_leq(self, arg)


class Lth(BinaryExpression):
    """
    This class represents comparison of two expressions using the
    less-than comparison operator. The effect of such an expression is a
    boolean value that is true if the left operand is less than the right
    operand. It is false otherwise.
    """

    def accept(self, visitor, arg):
        """
        Example:
        >>> n1 = Num(3)
        >>> n2 = Num(4)
        >>> e = Lth(n1, n2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        True

        >>> n1 = Num(3)
        >>> n2 = Num(3)
        >>> e = Lth(n1, n2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        False

        >>> n1 = Num(4)
        >>> n2 = Num(3)
        >>> e = Lth(n1, n2)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        False
        """
        return visitor.visit_lth(self, arg)


class UnaryExpression(Expression):
    """
    This class represents unary expressions. A unary expression has only one
    sub-expression.
    """

    def __init__(self, exp):
        self.exp = exp

    @abstractmethod
    def accept(self, visitor, arg):
        raise NotImplementedError


class Neg(UnaryExpression):
    """
    This expression represents the additive inverse of a number. The additive
    inverse of a number n is the number -n, so that the sum of both is zero.
    """

    def accept(self, visitor, arg):
        """
        Example:
        >>> n = Num(3)
        >>> e = Neg(n)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        -3

        >>> n = Num(0)
        >>> e = Neg(n)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        0
        """
        return visitor.visit_neg(self, arg)


class Not(UnaryExpression):
    """
    This expression represents the negation of a boolean. The negation of a
    boolean expression is the logical complement of that expression.
    """

    def accept(self, visitor, arg):
        """
        Example:
        >>> t = Bln(True)
        >>> e = Not(t)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        False

        >>> t = Bln(False)
        >>> e = Not(t)
        >>> ev = EvalVisitor()
        >>> e.accept(ev, None)
        True
        """
        return visitor.visit_not(self, arg)


class Let(Expression):
    """
    This class represents a let expression. The semantics of a let expression,
    such as "let v <- e0 in e1" on an environment env is as follows:
    1. Evaluate e0 in the environment env, yielding e0_val
    2. Evaluate e1 in the new environment env' = env + {v:e0_val}
    """

    def __init__(self, identifier, exp_def, exp_body):
        self.identifier = identifier
        self.exp_def = exp_def
        self.exp_body = exp_body

    def accept(self, visitor, arg):
        """
        Example:
        >>> e = Let('v', Num(42), Var('v'))
        >>> ev = EvalVisitor()
        >>> e.accept(ev, {})
        42

        >>> e = Let('v', Num(40), Let('w', Num(2), Add(Var('v'), Var('w'))))
        >>> ev = EvalVisitor()
        >>> e.accept(ev, {})
        42

        >>> e = Let('v', Add(Num(40), Num(2)), Mul(Var('v'), Var('v')))
        >>> ev = EvalVisitor()
        >>> e.accept(ev, {})
        1764
        """
        return visitor.visit_let(self, arg)


class Fn(Expression):
    """
    This class represents an anonymous function.

        >>> f = Fn('v', Mul(Var('v'), Var('v')))
        >>> ev = EvalVisitor()
        >>> print(f.accept(ev, {}))
        Fn(v)
    """

    def __init__(self, formal, body):
        self.formal = formal
        self.body = body

    def accept(self, visitor, arg):
        return visitor.visit_fn(self, arg)


class Fun(Expression):
    """
    This class represents a named function. Named functions can be invoked
    recursively.

        >>> f = Fun('f', 'v', Mul(Var('v'), Var('v')))
        >>> ev = EvalVisitor()
        >>> print(f.accept(ev, {}))
        Fun f(v)
    """

    def __init__(self, name, formal, body):
        self.name = name
        self.formal = formal
        self.body = body

    def accept(self, visitor, arg):
        return visitor.visit_fun(self, arg)


class App(Expression):
    """
    This class represents a function application, such as 'e0 e1'. The semantics
    of an application is as follows: we evaluate the left side, e.g., e0. It
    must result into a function fn(p, b) denoting a function that takes in a
    parameter p and evaluates a body b. We then evaluates e1, to obtain a value
    v. Finally, we evaluate b, but in a context where p is bound to v.

    Examples:
        >>> f = Fn('v', Mul(Var('v'), Var('v')))
        >>> e = App(f, Add(Num(40), Num(2)))
        >>> ev = EvalVisitor()
        >>> e.accept(ev, {})
        1764

        >>> f = Fn('v', Mul(Var('v'), Var('w')))
        >>> e = Let('w', Num(3), App(f, Num(2)))
        >>> ev = EvalVisitor()
        >>> e.accept(ev, {})
        6

        >>> e = Let('f', Fn('x', Add(Var('x'), Num(1))), App(Var('f'), Num(1)))
        >>> ev = EvalVisitor()
        >>> e.accept(ev, {})
        2

        >>> e0 = Let('w', Num(3), App(Var('f'), Num(1)))
        >>> e1 = Let('f', Fn('v', Add(Var('v'), Var('w'))), e0)
        >>> e2 = Let('w', Num(2), e1)
        >>> ev = EvalVisitor()
        >>> e2.accept(ev, {})
        3

        >>> e0 = Fun('f', 'v', Mul(Var('v'), Var('v')))
        >>> e1 = Add(Num(3), Num(4))
        >>> e2 = App(e0, e1)
        >>> ev = EvalVisitor()
        >>> print(e2.accept(ev, {}))
        49
    """

    def __init__(self, function, actual):
        self.function = function
        self.actual = actual

    def accept(self, visitor, arg):
        return visitor.visit_app(self, arg)


class IfThenElse(Expression):
    """
    This class represents a conditional expression. The semantics an expression
    such as 'if B then E0 else E1' is as follows:
    1. Evaluate B. Call the result ValueB.
    2. If ValueB is True, then evalute E0 and return the result.
    3. If ValueB is False, then evaluate E1 and return the result.
    Notice that we only evaluate one of the two sub-expressions, not both. Thus,
    "if True then 0 else 1 div 0" will return 0 indeed.
    """

    def __init__(self, cond, e0, e1):
        self.cond = cond
        self.e0 = e0
        self.e1 = e1

    def accept(self, visitor, arg):
        """
        Example:
        >>> e = IfThenElse(Bln(True), Num(42), Num(30))
        >>> ev = EvalVisitor()
        >>> e.accept(ev, {})
        42

        >>> e = IfThenElse(Bln(False), Num(42), Num(30))
        >>> ev = EvalVisitor()
        >>> e.accept(ev, {})
        30
        """
        return visitor.visit_ifThenElse(self, arg)