from typing import List


def count_ways(row: int, col: int) -> int:
    """
    1. Create 2d table to as "cache" table. table[i][j] contains number of ways to reach this coordinate from top-left.
    2. All cells in first row and first column have only one way to reach them.
    3. Any other columns possible ways is sum of ways to reach column on the left and ways to reach cell on the top of them.
    4. Build this table in bottom up manner. 
    """
    if row == 1 or col == 1:
        return 1

    ways_by_coordinate = [[0] * col] * row

    for i in range(row):
        ways_by_coordinate[i][0] = 1
    
    for i in range(col):
        ways_by_coordinate[0][i] = 1

    for i in range(1, row):
        for j in range(1, col):
            ways_by_coordinate[i][j] = ways_by_coordinate[i][j-1] + ways_by_coordinate[i-1][j]

    return ways_by_coordinate[row-1][col-1]


assert count_ways(2, 2) == 2
assert count_ways(2, 3) == 3
assert count_ways(5, 5) == 70
