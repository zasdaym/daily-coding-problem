package problem098

import "testing"

func TestFindWord(t *testing.T) {
	board := [][]byte{
		{'A', 'B', 'C', 'E'},
		{'S', 'F', 'C', 'S'},
		{'A', 'D', 'E', 'E'},
	}

	testCases := []struct {
		name     string
		target   string
		expected bool
	}{
		{
			name:     "existent word",
			target:   "ABCCED",
			expected: true,
		},
		{
			name:     "non-existent word",
			target:   "ABCA",
			expected: false,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := findWord(board, tc.target)
			if tc.expected != got {
				t.Errorf("want %v got %v", tc.expected, got)
			}
		})
	}
}
