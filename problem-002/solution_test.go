package problem002

import (
	"reflect"
	"testing"
)

func TestExclusiveProducts(t *testing.T) {
	testCases := []struct {
		name     string
		nums     []int
		expected []int
	}{
		{
			name:     "empty slice",
			nums:     []int{},
			expected: []int{},
		},
		{
			name:     "simple slice",
			nums:     []int{1, 2, 3, 4},
			expected: []int{24, 12, 8, 6},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := exclusiveProducts(tc.nums)
			if !reflect.DeepEqual(tc.expected, got) {
				t.Errorf("want %v, got %v", tc.expected, got)
			}
		})
	}
}
