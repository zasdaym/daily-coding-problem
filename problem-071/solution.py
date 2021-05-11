from random import randint


def rand5() -> int:
    return randint(1, 5)


def rand7() -> int:
    """
    Imagine a 5x5 array consists of numbers from 1 to 25.
    We use the rand5 function to randomly select the row and col of the imaginary array.
    """

    row, col = rand5() - 1, rand5()
    n = (5 * row) + col
    if n > 21:
        return rand7()
    else:
        return n % 7
