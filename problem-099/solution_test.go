package problem099

import "testing"

func TestLongestConsecutiveLength(t *testing.T) {
	testCases := []struct {
		name     string
		nums     []int
		expected int
	}{
		{
			name:     "separated consecutive sequence",
			nums:     []int{100, 4, 200, 1, 3, 2},
			expected: 4,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := longestConsecutiveLength(tc.nums)
			if tc.expected != got {
				t.Errorf("want %d got %d", tc.expected, got)
			}
		})
	}
}
