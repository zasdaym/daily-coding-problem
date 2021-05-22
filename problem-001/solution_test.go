package problem001

import "testing"

func TestTwoSum(t *testing.T) {
	testCases := []struct {
		name     string
		nums     []int
		target   int
		expected bool
	}{
		{
			name:     "pair exists",
			nums:     []int{1, 4, 3, 8, 5},
			target:   6,
			expected: true,
		},
		{
			name:     "pair does not exist",
			nums:     []int{1, 4, 3, 8, 5},
			target:   3,
			expected: false,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := twoSum(tc.nums, tc.target)
			if tc.expected != got {
				t.Errorf("want %v got %v", tc.expected, got)
			}
		})
	}
}
