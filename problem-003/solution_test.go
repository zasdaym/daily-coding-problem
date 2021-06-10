package problem003

import (
	"fmt"
	"testing"
)

func TestSerialize(t *testing.T) {
	testCases := []struct {
		name     string
		root     *treeNode
		expected string
	}{
		{
			name:     "empty tree",
			root:     nil,
			expected: "end",
		},
		{
			name: "simple tree",
			root: &treeNode{
				val: "A",
				left: &treeNode{
					val: "B",
					left: &treeNode{
						val: "C",
					},
					right: &treeNode{
						val: "D",
					},
				},
				right: &treeNode{
					val: "Z",
				},
			},
			expected: "A,B,C,end,end,D,end,end,Z,end,end",
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := serialize(tc.root)
			if tc.expected != got {
				t.Errorf("want %v got %v", tc.expected, got)
			}
		})
	}
}

func TestDeserialize(t *testing.T) {
	testCases := []struct {
		name     string
		s        string
		expected *treeNode
	}{
		{
			name:     "empty string",
			s:        "",
			expected: nil,
		},
		{
			name: "simple string",
			s:    "A,B,C,end,end,D,end,end,Z,end,end",
			expected: &treeNode{
				val: "A",
				left: &treeNode{
					val: "B",
					left: &treeNode{
						val: "C",
					},
					right: &treeNode{
						val: "D",
					},
				},
				right: &treeNode{
					val: "Z",
				},
			},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := deserialize(tc.s)
			if !isSameTree(tc.expected, got) {
				t.Errorf("want %v, got %v", tc.expected, got)
			}
		})
	}
}

func isSameTree(a, b *treeNode) bool {
	if a == nil && b == nil {
		return true
	}

	if a == nil {
		fmt.Printf("a tree nil when b is %s", b.val)
		return false
	}

	if b == nil {
		fmt.Printf("b tree nil when a is %s", a.val)
		return false
	}

	if a.val != b.val {
		fmt.Printf("%s is not %s", a.val, b.val)
		return false
	}

	return isSameTree(a.left, b.left) && isSameTree(a.right, b.right)
}
