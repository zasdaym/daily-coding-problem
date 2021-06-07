package problem098

import "strings"

func findWord(grid [][]rune, target string) bool {
	if len(grid) == 0 {
		return false
	}

	rowLength := len(grid)
	colLength := len(grid[0])

	for _, row := range grid {
		word := string(row)
		if strings.Contains(word, target) {
			return true
		}
	}

	for col := 0; col < colLength; col++ {
		var chars []rune
		for row := 0; row < rowLength; row++ {
			chars = append(chars, grid[row][col])
		}
		word := string(chars)
		if strings.Contains(word, target) {
			return true
		}
	}

	return false
}
