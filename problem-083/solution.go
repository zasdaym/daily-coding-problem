package problem083

type treeNode struct {
	val   int
	left  *treeNode
	right *treeNode
}

// invertTree inverts a binary tree in-place.
func invertTree(root *treeNode) {
	if root == nil {
		return
	}

	invertTree(root.left)
	invertTree(root.right)
	root.left, root.right = root.right, root.left
}
