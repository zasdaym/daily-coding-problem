package problem004

import "testing"

func TestLowestMissingPositive(t *testing.T) {
	testCases := []struct {
		name     string
		nums     []int
		expected int
	}{
		{
			name:     "empty numbers",
			nums:     []int{},
			expected: 1,
		},
		{
			name:     "unsorted positive numbers",
			nums:     []int{5, 3, 1, 7, 8, 3},
			expected: 2,
		},
		{
			name:     "mixed negative and positive numbers",
			nums:     []int{5, -3, 1, -7, 8, 12},
			expected: 2,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := lowestMissingPositive(tc.nums)
			if tc.expected != got {
				t.Errorf("want %d got %d", tc.expected, got)
			}
		})
	}
}
