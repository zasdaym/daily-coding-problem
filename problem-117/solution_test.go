package problem117

import "testing"

func TestMinLevelSum(t *testing.T) {
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
			name: "min sum on level 1",
			root: &treeNode{
				val: 15,
				left: &treeNode{
					val: 1,
					left: &treeNode{
						val: 4,
					},
				},
				right: &treeNode{
					val: 2,
					left: &treeNode{
						val: 6,
					},
					right: &treeNode{
						val: 8,
					},
				},
			},
			expected: 1,
		},
		{
			name: "min sum on last level",
			root: &treeNode{
				val: 15,
				left: &treeNode{
					val: 6,
					left: &treeNode{
						val: 4,
					},
				},
				right: &treeNode{
					val: 2,
					left: &treeNode{
						val: 1,
					},
					right: &treeNode{
						val: 1,
					},
				},
			},
			expected: 2,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := minLevelSum(tc.root)
			if tc.expected != got {
				t.Errorf("want %v got %v", tc.expected, got)
			}
		})
	}
}
