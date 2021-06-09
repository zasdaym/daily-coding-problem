package problem100

import (
	"testing"
)

func TestCoverPoints(t *testing.T) {
	testCases := []struct {
		name     string
		points   []point
		expected int
	}{
		{
			name:     "empty points",
			points:   []point{},
			expected: 0,
		},
		{
			name: "three points",
			points: []point{
				{x: 0, y: 0},
				{x: 1, y: 1},
				{x: 1, y: 2},
			},
			expected: 2,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := coverPoints(tc.points)
			if tc.expected != got {
				t.Errorf("want %v got %v", tc.expected, got)
			}
		})
	}
}
