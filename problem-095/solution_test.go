package problem095

import (
	"reflect"
	"testing"
)

func TestNextPermutation(t *testing.T) {
	testCases := []struct {
		name     string
		nums     []int
		expected []int
	}{
		{
			name:     "unsorted numbers",
			nums:     []int{4, 3, 2, 5, 1},
			expected: []int{4, 3, 5, 1, 2},
		},
		{
			name:     "sorted numbers",
			nums:     []int{1, 2, 3, 4, 5},
			expected: []int{1, 2, 3, 5, 4},
		},
		{
			name:     "reverse sorted numbers",
			nums:     []int{5, 4, 3, 2, 1},
			expected: []int{1, 2, 3, 4, 5},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			nextPermutation(tc.nums)
			if !reflect.DeepEqual(tc.expected, tc.nums) {
				t.Errorf("want %v got %v", tc.expected, tc.nums)
			}
		})
	}
}
