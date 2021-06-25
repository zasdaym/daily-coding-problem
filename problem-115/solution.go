package problem115

type treeNode struct {
	val         int
	left, right *treeNode
}

func isSameSubtree(s *treeNode, t *treeNode) bool {
	return isSameTree(s, t) || isSameTree(s.left, t) || isSameTree(s.right, t)
}

func isSameTree(a *treeNode, b *treeNode) bool {
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
