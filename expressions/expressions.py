"""Module which implements an Expression Tree Class Hierachy."""
from numbers import Number as Num


class Expression:
    """Parent of Terminal and Operator."""

    def __init__(self, *operands):
        """Construct an Expression."""
        self.operands = operands

    def __add__(self, expr):
        """Add: self + expr."""
        return Add(self, expr)

    def __sub__(self, expr):
        """Subtract: self - expr."""
        return Sub(self, expr)

    def __mul__(self, expr):
        """Multiple: self * expr."""
        return Mul(self, expr)

    def __truediv__(self, expr):
        """Divide: self / expr."""
        return Div(self, expr)

    def __pow__(self, expr):
        """Power: self ^ expr."""
        return Pow(self, expr)


class Terminal(Expression):
    """Terminal class: parent of Number and Symbol."""

    precedence = 4

    def __init__(self, val):
        """Construct a terminal."""
        self.val = val
        super().__init__(())

    def __repr__(self):
        """Repr method."""
        return repr(self.val)

    def __str__(self):
        """Str method."""
        return str(self.val)


class Number(Terminal):
    """Number class. A terminal represented by a Num."""

    def __init__(self, val):
        """Construct a Number expression."""
        if not isinstance(val, Num):
            raise TypeError("Val input of type: " + type(val).__name__ +
                            "Expected val of type " + type(Number).__name__ +
                            ".")
        super().__init__(val)


class Symbol(Terminal):
    """Symbol class. A terminal represented by a Str."""

    def __init__(self, val):
        """Construct a Symbol."""
        if not isinstance(val, str):
            raise TypeError("Val input of type: " + type(val).__name__ +
                            "Expected val of type " + type(str).__name__ + ".")
        super().__init__(val)


class Operator(Expression):
    """Operator class."""

    def __repr__(self):
        """Repr method."""
        return type(self).__name__ + repr(self.operands)

    def __str__(self):
        """Str method."""
        return str(self.operands[0]) + " " + self.exp_symbol\
            + " " + str(self.operands[1])


class Add(Operator):
    """Addition operator."""

    exp_symbol = "+"
    precedence = 3


class Mul(Operator):
    """Multiplication Operation."""

    exp_symbol = "*"
    precedence = 2


class Sub(Operator):
    """Subtraction Operator."""

    exp_symbol = "-"
    precedence = 3


class Div(Operator):
    """Division Operator."""

    exp_symbol = "/"
    precedence = 2


class Pow(Operator):
    """Power Operator."""

    exp_symbol = "^"
    precedence = 1
