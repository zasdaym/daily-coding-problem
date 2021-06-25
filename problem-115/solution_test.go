package problem115

import (
	"testing"
)

func TestIsSameSubtree(t *testing.T) {
	testCases := []struct {
		name     string
		s, t     *treeNode
		expected bool
	}{
		{
			name: "same root tree",
			s: &treeNode{
				val: 1,
				left: &treeNode{
					val: 2,
				},
				right: &treeNode{
					val: 3,
				},
			},
			t: &treeNode{
				val: 1,
				left: &treeNode{
					val: 2,
				},
				right: &treeNode{
					val: 3,
				},
			},
			expected: true,
		},
		{
			name: "same subtree",
			s: &treeNode{
				val: 13,
				left: &treeNode{
					val: 4,
				},
				right: &treeNode{
					val: 1,
					left: &treeNode{
						val: 2,
					},
					right: &treeNode{
						val: 3,
					},
				},
			},
			t: &treeNode{
				val: 1,
				left: &treeNode{
					val: 2,
				},
				right: &treeNode{
					val: 3,
				},
			},
			expected: true,
		},
		{
			name: "different tree",
			s: &treeNode{
				val: 1,
				left: &treeNode{
					val: 2,
				},
				right: &treeNode{
					val: 3,
				},
			},
			t: &treeNode{
				val: 1,
				left: &treeNode{
					val: 2,
				},
				right: &treeNode{
					val: 5,
				},
			},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := isSameSubtree(tc.s, tc.t)
			if tc.expected != got {
				t.Errorf("want %v got %v", tc.expected, got)
			}
		})
	}
}
