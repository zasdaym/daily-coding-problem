from typing import List


def n_queens(n: int, board: List[int] = []) -> int:
    """
    Using backtracking technique.
    Board modelled as an array. Where the index is row number,
    and the value is column position where the queen is placed on that row.
    For each row, try placing a queen in column 0..N and check if the board is valid after each placement.
    Column number will be appended to the board array.
    If board is valid after placement, recursively call self with new board.
    But if not, remove the appended col number from board array, and try another column.
    """
    if n == len(board):
        return 1

    count = 0
    for col in range(n):
        board.append(col)
        if is_valid(board):
            count += n_queens(n, board)
        board.pop()
    return count


def is_valid(board: List[int]) -> bool:
    """
    Check if no queens attack each other in a board.
    """
    # get last queen position.
    current_queen_row, current_queen_col = len(board) - 1, board[-1]
    # for every another queeen
    for row, col in enumerate(board[:-1]):
        # is in the same col?
        diff = abs(current_queen_col - col)
        # is in the same diagonal?
        if diff == 0 or diff == current_queen_row - row:
            return False
    return True


assert n_queens(4) == 2
assert n_queens(5) == 10
assert n_queens(6) == 4
