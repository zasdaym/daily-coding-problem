from typing import List


def find_word(matrix: List[List[str]], target: str) -> bool:
    """
    1. Check string per row, check if target is substring of the current word.
    2. Check string per col, check if target is substring of the current word.
    """

    if not matrix:
        return False

    for row in matrix:
        if target in row:
            return True

    for col in range(len(matrix[0])):
        word = ""
        for row in range(len(matrix)):
            word += matrix[row][col]
        if target in word:
            return True

    return False


test_matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']
]

assert find_word(test_matrix, "FOAM")
assert find_word(test_matrix, "BNA")
assert not find_word(test_matrix, "OAX")
