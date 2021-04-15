from random import randint


def rand5() -> int:
    return randint(1, 5)


def rand7() -> int:
    """
    Randomly get an integer from a 5x5 array.
    """
    index = 22
    while index > 21:
        index = rand5() + (rand5() - 1) * 5
    return 1 + (index - 1) % 7
