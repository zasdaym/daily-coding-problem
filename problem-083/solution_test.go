package problem083

import "testing"

func TestInvertTree(t *testing.T) {
	testCases := []struct {
		name     string
		root     *treeNode
		expected *treeNode
	}{
		{
			name:     "empty tree",
			root:     nil,
			expected: nil,
		},
		{
			name: "same depth on both side",
			root: &treeNode{
				val: 5,
				left: &treeNode{
					val: 3,
				},
				right: &treeNode{
					val: 10,
				},
			},
			expected: &treeNode{
				val: 5,
				left: &treeNode{
					val: 10,
				},
				right: &treeNode{
					val: 3,
				},
			},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			invertTree(tc.root)
			if !isSameTree(tc.expected, tc.root) {
				t.Errorf("wrong invert, got different tree than expected")
			}
		})
	}
}

// isSameTree checks whether two binary tree have same value and structure.
func isSameTree(a, b *treeNode) bool {
	if a == nil && b == nil {
		return true
	}

	if a == nil || b == nil {
		return false
	}

	if a.val != b.val {
		return false
	}

	return isSameTree(a.left, b.left) && isSameTree(a.right, b.right)
}
