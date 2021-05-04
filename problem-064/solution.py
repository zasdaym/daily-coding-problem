from typing import List, Tuple


def knight_tours(board: List[List[int]], curr: Tuple[int, int], count: int) -> -1:
    """
    Currently this only solves a knight tour for a specific starting point.
    """
    if count == len(board) ** 2:
        return

    deltas = [
        (2, 1),
        (1, 2),
        (-2, 1),
        (-1, 2),
        (2, -1),
        (1, -2),
        (-2, -1),
        (-1, -2),
    ]

    for delta in deltas:
        next_x, next_y = curr[0] + delta[0], curr[1] + delta[1]
        if not is_valid_coordinate((next_x, next_y), len(board)):
            continue

        board[next_x][next_y] = count
        knight_tours(board, (next_x, next_y), count + 1)
        board[next_x][next_y] = -1


def is_valid_coordinate(coordinate: Tuple[int, int], board_size: int) -> bool:
    x, y = coordinate
    return 0 <= x < board_size and 0 <= y < board_size


test_board = [
    [-1, -1, -1, -1, 0, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1]
]

knight_tours(test_board, (0, 4), 1)
