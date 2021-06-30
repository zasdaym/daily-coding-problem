package problem009

import "testing"

func TestMaxNonAdjacentSum(t *testing.T) {
	testCases := []struct {
		name     string
		nums     []int
		expected int
	}{
		{
			name:     "empty numbers",
			nums:     []int{},
			expected: 0,
		},
		{
			name:     "even count numbers",
			nums:     []int{5, 1, 1, 5},
			expected: 10,
		},
		{
			name:     "odd count numbers",
			nums:     []int{2, 4, 6, 2, 5},
			expected: 13,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := maxNonAdjacentSum(tc.nums)
			if tc.expected != got {
				t.Errorf("want %d got %d", tc.expected, got)
			}
		})
	}
}
