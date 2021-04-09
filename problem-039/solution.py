from typing import List

def game_of_life(board: List[List[int]], count: int) -> None:
    """
    1. Iterate for each cell in board:
    2. Count live neighbors on a given cell.
    3. Here's the tricky part. Rather than directly marking live cell as 1 or dead cell as 0,
    we use 2 and -1. This is to differentiate the original state of the cell, so we can use
    the original cell state to determine other cell's state.
    4. Apply the game rule for each cell.
    5. Apply normalization for custom state (2 and -1) on all cells, and print it.
    6. Repeat for each game steps.
    """
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    rows = len(board)
    cols = len(board[0])

    for _ in range(count):
        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for neighbor in neighbors:
                    neighbor_row = row + neighbor[0]
                    neighbor_col = col + neighbor[1]
                    if (neighbor_row < rows and neighbor_row >= 0) and (neighbor_col < cols and neighbor_col >= 0) and abs(board[neighbor_row][neighbor_col]) == 1:
                        live_neighbors += 1
                    
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1
                
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2

                    
        for row in range(rows):
            for col in range(cols):
                char = "*"
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
                    char = "."
                print(char, end=" ")
            print("")
        
        print("")

test_board = [
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 0]
]
game_of_life(test_board, 3)