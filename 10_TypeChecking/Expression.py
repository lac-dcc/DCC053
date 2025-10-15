from abc import ABC, abstractmethod
from Visitor import *


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
        return visitor.visit_var(self, arg)


class Bln(Expression):
    """
    This class represents expressions that are boolean values. There are only
    two boolean values: true and false. The semantics of such an expression is
    the boolean itself.
    """

    def __init__(self, bln):
        self.bln = bln

    def accept(self, visitor, arg):
        return visitor.visit_bln(self, arg)


class Num(Expression):
    """
    This class represents expressions that are numbers. The semantics of such
    an expression is the number itself.
    """

    def __init__(self, num):
        self.num = num

    def accept(self, visitor, arg):
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
    This class represents the equality between two expressions. The semantics
    of such an expression is True if the subexpressions are the same, or false
    otherwise.
    """

    def accept(self, visitor, arg):
        return visitor.visit_eql(self, arg)


class Add(BinaryExpression):
    """
    This class represents addition of two expressions. The semantics of such
    an expression is the addition of the two subexpression's values.
    """

    def accept(self, visitor, arg):
        return visitor.visit_add(self, arg)


class And(BinaryExpression):
    """
    This class represents the logical disjunction of two boolean expressions.
    The evaluation of an expression of this kind is the logical AND of the two
    subexpression's values.
    """

    def accept(self, visitor, arg):
        return visitor.visit_and(self, arg)


class Or(BinaryExpression):
    """
    This class represents the logical conjunction of two boolean expressions.
    The evaluation of an expression of this kind is the logical OR of the two
    subexpression's values.
    """

    def accept(self, visitor, arg):
        return visitor.visit_or(self, arg)


class Sub(BinaryExpression):
    """
    This class represents subtraction of two expressions. The semantics of such
    an expression is the subtraction of the two subexpression's values.
    """

    def accept(self, visitor, arg):
        return visitor.visit_sub(self, arg)


class Mul(BinaryExpression):
    """
    This class represents multiplication of two expressions. The semantics of
    such an expression is the product of the two subexpression's values.
    """

    def accept(self, visitor, arg):
        return visitor.visit_mul(self, arg)


class Div(BinaryExpression):
    """
    This class represents the integer division of two expressions. The
    semantics of such an expression is the integer quocient of the two
    subexpression's values.
    """

    def accept(self, visitor, arg):
        return visitor.visit_div(self, arg)


class Leq(BinaryExpression):
    """
    This class represents comparison of two expressions using the
    less-than-or-equal comparator. The semantics of such an expression is a
    boolean value that is true if the left operand is less than or equal the
    right operand. It is false otherwise.
    """

    def accept(self, visitor, arg):
        return visitor.visit_leq(self, arg)


class Lth(BinaryExpression):
    """
    This class represents comparison of two expressions using the
    less-than comparison operator. The semantics of such an expression is a
    boolean value that is true if the left operand is less than the right
    operand. It is false otherwise.
    """

    def accept(self, visitor, arg):
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
        return visitor.visit_neg(self, arg)


class Not(UnaryExpression):
    """
    This expression represents the negation of a boolean. The negation of a
    boolean expression is the logical complement of that expression.
    """

    def accept(self, visitor, arg):
        return visitor.visit_not(self, arg)


class Let(Expression):
    """
    This class represents a let expression.
    """

    def __init__(self, identifier, tp_var, exp_def, exp_body):
        self.identifier = identifier
        self.tp_var = tp_var
        self.exp_def = exp_def
        self.exp_body = exp_body

    def accept(self, visitor, arg):
        return visitor.visit_let(self, arg)


class Fn(Expression):
    """
    This class represents an anonymous function.
    """

    def __init__(self, formal, tp_var, body):
        self.formal = formal
        self.tp_var = tp_var
        self.body = body

    def accept(self, visitor, arg):
        return visitor.visit_fn(self, arg)


class App(Expression):
    """
    This class represents a function application, such as 'e0 e1'.
    """

    def __init__(self, function, actual):
        self.function = function
        self.actual = actual

    def accept(self, visitor, arg):
        return visitor.visit_app(self, arg)


class IfThenElse(Expression):
    """
    This class represents a conditional expression.
    """

    def __init__(self, cond, e0, e1):
        self.cond = cond
        self.e0 = e0
        self.e1 = e1

    def accept(self, visitor, arg):
        return visitor.visit_ifThenElse(self, arg)