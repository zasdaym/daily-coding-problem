package problem118

import (
	"reflect"
	"testing"
)

func TestSortSquared(t *testing.T) {
	testCases := []struct {
		name     string
		nums     []int
		expected []int
	}{
		{
			name:     "empty numbers",
			nums:     nil,
			expected: nil,
		},
		{
			name:     "positive numbers",
			nums:     []int{1, 2, 4, 5},
			expected: []int{1, 4, 16, 25},
		},
		{
			name:     "positive and negative numbers",
			nums:     []int{-5, 1, 2, 4},
			expected: []int{1, 4, 16, 25},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := sortSquared(tc.nums)
			if !reflect.DeepEqual(tc.expected, got) {
				t.Errorf("want %v got %v", tc.expected, got)
			}
		})
	}
}
