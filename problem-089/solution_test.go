package problem089

import "testing"

func TestIsValidBinarySearchTree(t *testing.T) {
	testCases := []struct {
		name     string
		root     *treeNode
		expected bool
	}{
		{
			name:     "empty tree",
			root:     nil,
			expected: true,
		},
		{
			name: "valid binary tree",
			root: &treeNode{
				val: 5,
				left: &treeNode{
					val: 1,
				},
				right: &treeNode{
					val: 8,
				},
			},
			expected: true,
		},
		{
			name: "invalid binary tree",
			root: &treeNode{
				val: 5,
				left: &treeNode{
					val: 4,
				},
				right: &treeNode{
					val: 9,
					left: &treeNode{
						val: 4,
					},
				},
			},
			expected: false,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := isValidBinarySearchTree(tc.root)
			if tc.expected != got {
				t.Errorf("want %v got %v", tc.expected, got)
			}
		})
	}
}
