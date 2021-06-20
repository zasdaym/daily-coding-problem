package problem110

import (
	"reflect"
	"testing"
)

func TestGetAllPaths(t *testing.T) {
	testCases := []struct {
		name     string
		root     *treeNode
		expected [][]int
	}{
		{
			name:     "empty tree",
			root:     nil,
			expected: [][]int{},
		},
		{
			name: "valid tree",
			root: &treeNode{
				val: 1,
				left: &treeNode{
					val: 2,
				},
				right: &treeNode{
					val: 3,
					left: &treeNode{
						val: 4,
					},
					right: &treeNode{
						val: 5,
					},
				},
			},
			expected: [][]int{
				{1, 2},
				{1, 3, 4},
				{1, 3, 5},
			},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := getAllPaths(tc.root)
			if !reflect.DeepEqual(tc.expected, got) {
				t.Errorf("want %v got %v", tc.expected, got)
			}
		})
	}
}
