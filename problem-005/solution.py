def cons(a, b):
    """
    Given two parameters, return a function that accepts a function and run it with previous parameters
    """
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    """
    Return first parameter.
    """
    return pair(lambda a, b: a)


def cdr(pair):
    """
    Return second parameter.
    """
    return pair(lambda a, b: b)


assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
