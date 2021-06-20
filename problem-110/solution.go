package problem110

type treeNode struct {
	val   int
	left  *treeNode
	right *treeNode
}

func getAllPaths(root *treeNode) [][]int {
	return dfs(root, []int{}, [][]int{})
}

func dfs(root *treeNode, path []int, paths [][]int) [][]int {
	if root == nil {
		return paths
	}

	newPath := make([]int, len(path))
	copy(newPath, path)
	newPath = append(newPath, root.val)

	newPaths := make([][]int, len(paths))
	copy(newPaths, paths)

	if root.left == nil && root.right == nil {
		newPaths = append(newPaths, newPath)
		return newPaths
	}

	left_paths := dfs(root.left, newPath, paths)
	left_right_paths := dfs(root.right, newPath, left_paths)
	return left_right_paths
}
