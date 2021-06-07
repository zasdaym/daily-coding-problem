package problem098

import "testing"

func TestFindWord(t *testing.T) {
	testCases := []struct {
		name     string
		grid     [][]rune
		target   string
		expected bool
	}{
		{
			name: "existent word",
			grid: [][]rune{
				{'b', 'c', 'x', 'g', 'u'},
				{'p', 'a', 'p', 'e', 'o'},
				{'t', 'c', 'e', 'a', 'd'},
				{'k', 'i', 'x', 'r', 'v'},
			},
			target:   "gear",
			expected: true,
		},
		{
			name: "existent word",
			grid: [][]rune{
				{'b', 'c', 'x', 'g', 'u'},
				{'p', 'a', 'p', 'e', 'o'},
				{'t', 'c', 'e', 'a', 'd'},
				{'k', 'i', 'x', 'r', 'v'},
			},
			target:   "swim",
			expected: false,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := findWord(tc.grid, tc.target)
			if tc.expected != got {
				t.Errorf("want %v got %v", tc.expected, got)
			}
		})
	}
}
