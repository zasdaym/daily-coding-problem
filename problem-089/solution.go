package problem089

type treeNode struct {
	val         int
	left, right *treeNode
}

// isValidBinaryTree checks if given binary search tree is valid.
func isValidBinarySearchTree(root *treeNode) bool {
	if root == nil {
		return true
	}

	const maxInt = int(^uint(0) >> 1)
	const minInt = -maxInt - 1
	return isValidBinarySearchTreeHelper(root.left, minInt, root.val) && isValidBinarySearchTreeHelper(root.right, root.val, maxInt)
}

func isValidBinarySearchTreeHelper(root *treeNode, min, max int) bool {
	if root == nil {
		return true
	}

	if root.val > min && root.val <= max {
		return isValidBinarySearchTreeHelper(root.left, min, root.val) && isValidBinarySearchTreeHelper(root.right, root.val, max)
	}

	return false
}
