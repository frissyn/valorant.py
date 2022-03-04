import operator
import typing as t


attr = operator.attrgetter


class Expression:
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

        if op.startswith("."):
            self.func = lambda a, b: attr(op.strip("."))(a)(b)
        else:
            self.func = self.COMPARISONS[self.op]

    def __str__(self):
        return f"<Expression '{{object}} {self.expr}'>"

    def __repr(self):
        return self.__str__()

    def __bool__(self):
        return True


def exp(op: t.Text, value: t.Any) -> Expression:
    return Expression(op, value)
