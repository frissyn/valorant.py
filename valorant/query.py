import operator
import typing as t


attr = operator.attrgetter


class Expression:
    """Utility class for generating logical statements from a given operator and
    value. Supports `object <https://docs.python.org/3/library/operator.html#operator.lt>`_
    and `logical <https://docs.python.org/3/library/operator.html#operator.not_>`_
    operators. Also supports dot operators and member functions.

    :param op: The operator used to compare the element trait to the given value.
    :type op: Text

    :param value: The value to compare the element trait to.
    :type value: Any

    .. note::
        The Expression class only supports logical and object comparisons, and
        cannot generate "flipped" statements. (*i.e* ``is not`` works, but
        ``not in`` doesn't.)
    """

    COMPARISONS = {
        "!=": operator.ne,
        "<": operator.lt,
        "<=": operator.le,
        "==": operator.eq,
        ">": operator.gt,
        ">=": operator.ge,
        "in": operator.contains,
        "is not": operator.is_not,
        "is": operator.is_,
        "not": operator.not_,
    }

    def __init__(self, op: t.Text, value: t.Any):
        self.op = op
        self.value = value

    def statement(self, a: t.Any) -> bool:
        """Executes the generated logical statement against the passed value.

        **Examples:**

        .. code-block:: python

            exp = valorant.Expression('>=', 50)
            exp.statement(10) # => False

        .. code-block:: python

            exp = valorant.Expression('.endswith', '!')
            exp.statement("Hello, World!") # => True

        :param a: The value to test against.
        :type a: Any

        :rtype: bool
        """

        if self.op.startswith("."):
            return attr(self.op.strip("."))(a)(self.value)
        else:
            return self.COMPARISONS[self.op](a, self.value)

    def __str__(self):
        return f"<Expression '{{object}} {self.expr}'>"

    def __repr(self):
        return self.__str__()


def exp(op: t.Text, value: t.Any) -> Expression:
    """Shorthand method for creating expressions to use alongside :func:`ContentList.get`
    or :func:`ContentList.get_all`. Expressions can also be created directly.

    :param op: The operator used to compare the element trait to the given value.
    :type op: Text

    :param value: The value to compare the element trait to.
    :type value: Any

    :rtype: Expression
    """
    return Expression(op, value)
