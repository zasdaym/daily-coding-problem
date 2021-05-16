from typing import List, Set


def min_col_to_delete(matrix: List[str]) -> int:
    # edge case
    if not matrix:
        return 0

    col_to_delete = 0
    row_len, col_len = len(matrix), len(matrix[0])

    # check every col for unordered letters.
    for j in range(0, col_len):
        largest = matrix[0][j]
        for i in range(1, row_len):
            curr = matrix[i][j]
            if curr < largest:
                col_to_delete += 1
                break
            largest = curr

    return col_to_delete


tests = [
    [
        "cba",
        "daf",
        "ghi"
    ],
    [
        "abcdef"
    ],
    [
        "zyx",
        "wvu",
        "tsr"
    ]
]

expected_values = [1, 0, 3]

for i in range(len(tests)):
    assert min_col_to_delete(tests[i]) == expected_values[i]
