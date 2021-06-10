package problem008

type treeNode struct {
	val   int
	left  *treeNode
	right *treeNode
}

func countUnivalTree(root *treeNode) int {
	count, _ := helper(root, 0)
	return count
}

func helper(root *treeNode, count int) (int, bool) {
	if root == nil {
		return count, true
	}

	leftCount, isLeftUnival := helper(root.left, count)
	rightCount, isRightUnival := helper(root.right, count)

	totalCount := leftCount + rightCount

	if !isLeftUnival || !isRightUnival {
		return totalCount, false
	}

	if root.left != nil && root.val != root.left.val {
		return totalCount, false
	}

	if root.right != nil && root.val != root.right.val {
		return totalCount, false
	}

	return totalCount + 1, true
}
