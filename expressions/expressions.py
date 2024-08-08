"""Module which implements an Expression Tree Class Hierachy."""
from numbers import Number as Num


class Expression:
    """Parent of Terminal and Operator."""

    def __init__(self, *operands):
        """Construct an Expression."""
        self.operands = operands

    def __add__(self, expr):
        """Add: self + expr."""
        if isinstance(expr, Num):
            expr = Number(expr)
        if isinstance(self, Number):
            return Number(self.value + expr.value)
        return Add(self, expr)

    def __radd__(self, expr):
        """Add: expr + self."""
        expr = Number(expr)
        return Add(expr, self)

    def __sub__(self, expr):
        """Subtract: self - expr."""
        if isinstance(expr, Num):
            expr = Number(expr)
        if isinstance(self, Number):
            return Number(self.value - expr.value)
        return Sub(self, expr)

    def __rsub__(self, expr):
        """Add: expr + self."""
        expr = Number(expr)
        return Sub(expr, self)

    def __mul__(self, expr):
        """Multiple: self * expr."""
        if isinstance(expr, Num):
            expr = Number(expr)
        if isinstance(self, Number):
            return Number(self.value * expr.value)
        return Mul(self, expr)

    def __rmul__(self, expr):
        """Multiply: expr * self."""
        expr = Number(expr)
        return Mul(expr, self)

    def __truediv__(self, expr):
        """Divide: self / expr."""
        if isinstance(expr, Num):
            expr = Number(expr)
        if isinstance(self, Number):
            return Number(self.value / expr.value)
        return Div(self, expr)

    def __rtruediv__(self, expr):
        """Divide: expr / self."""
        expr = Number(expr)
        return Div(expr, self)

    def __pow__(self, expr):
        """Power: self ^ expr."""
        if isinstance(expr, Num):
            expr = Number(expr)
        if isinstance(self, Number):
            return Number(self.value ** expr.value)
        return Pow(self, expr)

    def __rpow__(self, expr):
        """Pow: expr ^ self."""
        expr = Number(expr)
        return Pow(expr, self)


class Terminal(Expression):
    """Terminal class: parent of Number and Symbol."""

    precedence = 0

    def __init__(self, value):
        """Construct a terminal."""
        self.value = value
        super().__init__()

    def __repr__(self):
        """Repr method."""
        return repr(self.value)

    def __str__(self):
        """Str method."""
        return str(self.value)


class Number(Terminal):
    """Number class. A terminal represented by a Num."""

    def __init__(self, value):
        """Construct a Number expression."""
        if not isinstance(value, Num):
            raise TypeError("Val input of type: " + type(value).__name__ +
                            "Expected val of type " + type(Number).__name__ +
                            ".")
        super().__init__(value)


class Symbol(Terminal):
    """Symbol class. A terminal represented by a Str."""

    def __init__(self, value):
        """Construct a Symbol."""
        if not isinstance(value, str):
            raise TypeError("Val input of type: " + type(value).__name__ +
                            "Expected val of type " + type(str).__name__ + ".")
        super().__init__(value)


class Operator(Expression):
    """Operator class."""

    def __repr__(self):
        """Repr method."""
        return type(self).__name__ + repr(self.operands)

    def __str__(self):
        """Str method."""
        a, b = self.operands[0], self.operands[1]
        if a.precedence > self.precedence:
            a_str = "(" + str(a) + ")"
        else:
            a_str = str(a)
        if b.precedence > self.precedence:
            b_str = "(" + str(b) + ")"
        else:
            b_str = str(b)
        return a_str + " " + self.exp_symbol + " " + b_str


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
