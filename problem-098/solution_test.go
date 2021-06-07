package problem098

import (
	"testing"
)

func TestFindWord(t *testing.T) {
	board := [][]byte{
		{'A', 'B', 'C', 'E'},
		{'S', 'F', 'C', 'S'},
		{'A', 'D', 'E', 'E'},
	}

	testCases := []struct {
		name     string
		board    [][]byte
		target   string
		expected bool
	}{
		{
			name:     "empty board",
			board:    [][]byte{},
			target:   "randomstring",
			expected: false,
		},
		{
			name:     "existent word",
			board:    board,
			target:   "ABCCED",
			expected: true,
		},
		{
			name:     "non-existent word",
			board:    board,
			target:   "ABCA",
			expected: false,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := findWord(tc.board, tc.target)
			if tc.expected != got {
				t.Errorf("want %v got %v", tc.expected, got)
			}
		})
	}
}
