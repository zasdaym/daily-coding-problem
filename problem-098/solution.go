package problem098

type coordinate struct {
	x, y int
}

func findWord(board [][]byte, target string) bool {
	if len(board) == 0 {
		return false
	}

	rowLength := len(board)
	colLength := len(board[0])

	for i := 0; i < rowLength; i++ {
		for j := 0; j < colLength; j++ {
			visited := make(map[coordinate]bool)
			coor := coordinate{i, j}
			if search(board, coor, target, 0, visited) {
				return true
			}
		}
	}

	return false
}

func search(board [][]byte, coor coordinate, target string, targetIdx int, visited map[coordinate]bool) bool {
	if !isValid(board, coor) {
		return false
	}

	if visited[coor] {
		return false
	}

	if board[coor.x][coor.y] != target[targetIdx] {
		return false
	}

	if targetIdx == len(target)-1 {
		return true
	}

	visited[coor] = true

	deltas := []coordinate{
		{0, 1},
		{0, -1},
		{1, 0},
		{-1, 0},
	}

	for _, delta := range deltas {
		nextCoor := coordinate{
			x: coor.x + delta.x,
			y: coor.y + delta.y,
		}
		if search(board, nextCoor, target, targetIdx+1, visited) {
			return true
		}
	}

	delete(visited, coor)
	return false
}

func isValid(board [][]byte, coor coordinate) bool {
	return coor.x >= 0 && coor.x < len(board) && coor.y >= 0 && coor.y < len(board[0])
}
