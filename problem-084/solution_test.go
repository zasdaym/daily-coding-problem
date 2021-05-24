package problem084

import "testing"

func TestCountIslands(t *testing.T) {
	testCases := []struct {
		name     string
		grid     [][]int
		expected int
	}{
		{
			name:     "empty grid",
			grid:     nil,
			expected: 0,
		},
		{
			name: "simple grid",
			grid: [][]int{
				{1, 0, 0, 0, 0},
				{0, 0, 1, 1, 0},
				{0, 1, 1, 0, 0},
				{1, 1, 0, 0, 1},
				{1, 1, 0, 0, 1},
			},
			expected: 4,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := countIslands(tc.grid)
			if tc.expected != got {
				t.Errorf("want %d got %d", tc.expected, got)
			}
		})
	}
}
