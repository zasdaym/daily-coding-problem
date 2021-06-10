package problem008

import "testing"

func TestCountUnivalTree(t *testing.T) {
	testCases := []struct {
		name     string
		root     *treeNode
		expected int
	}{
		{
			name:     "empty tree",
			root:     nil,
			expected: 0,
		},
		{
			name: "unbalanced tree",
			root: &treeNode{
				val: 0,
				left: &treeNode{
					val: 1,
				},
				right: &treeNode{
					val: 0,
					left: &treeNode{
						val: 1,
						left: &treeNode{
							val: 1,
						},
						right: &treeNode{
							val: 1,
						},
					},
					right: &treeNode{
						val: 0,
					},
				},
			},
			expected: 5,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := countUnivalTree(tc.root)
			if tc.expected != got {
				t.Errorf("want %v got %v", tc.expected, got)
			}
		})
	}
}
