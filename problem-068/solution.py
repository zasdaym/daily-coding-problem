from typing import Dict, List, Tuple, Set


def bishop_attacks(board_size: int, bishops: List[Tuple[int, int]]) -> int:
    # initialize board
    board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    for bishop in bishops:
        row, col = bishop
        board[row][col] = 1

    pairs: Set[Tuple[Tuple[int, int], Tuple[int, int]]] = set()

    # for every bishop
    for bishop in bishops:
        deltas = [
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]

        # check every direction
        for delta in deltas:
            neighbor = bishop
            # check until end of the board (or more, unoptimal)
            for i in range(board_size):
                # out of board
                neighbor = (neighbor[0] + delta[0], neighbor[1] + delta[1])
                if not is_valid_coordinate(board_size, neighbor):
                    continue

                # no bishop
                row, col = neighbor
                if board[row][col] == 0:
                    continue

                # order the pair before insert into set, to prevent duplicate
                if bishop[0] < neighbor[0]:
                    pairs.add((bishop, neighbor))
                else:
                    pairs.add((neighbor, bishop))

    return len(pairs)


def is_valid_coordinate(board_size: int, coordinate: Tuple[int, int]) -> bool:
    row, col = coordinate
    return 0 <= row < board_size and 0 <= col < board_size


test_bishops = [
    (0, 0),
    (1, 2),
    (2, 2),
    (4, 0),
    (4, 4)
]

assert bishop_attacks(5, test_bishops) == 4
