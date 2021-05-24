package problem084

// countIslands counts number of islands in given grid
// of land (represented in 1) and water (represented by 0).
// Island is a group of 1 that are surrounded by 0.
func countIslands(grid [][]int) int {
	if len(grid) == 0 {
		return 0
	}

	count := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] != 1 {
				continue
			}
			dfs(grid, i, j)
			count += 1
		}
	}

	return count
}

// dfs visits neighboring cells recursively until perimeter
// or already visited cell is found.
func dfs(grid [][]int, row, col int) {
	// check if out of bound and cell is an unvisited islan
	if row < 0 || col < 0 || row >= len(grid) || col >= len(grid[0]) || grid[row][col] != 1 {
		return
	}

	// mark cell as visited
	grid[row][col] = 2

	// check neighbors
	dfs(grid, row+1, col)
	dfs(grid, row-1, col)
	dfs(grid, row, col+1)
	dfs(grid, row, col-1)
}
