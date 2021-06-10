package problem003

import (
	"fmt"
	"strings"
)

type treeNode struct {
	val   string
	left  *treeNode
	right *treeNode
}

// serialize takes a root node and serializes it into a string
// represenration with inorder traversal.
// Each node will be separated by comma, and null represented with "end".
func serialize(root *treeNode) string {
	if root == nil {
		return "end"
	}

	left := serialize(root.left)
	right := serialize(root.right)
	return fmt.Sprintf("%s,%s,%s", root.val, left, right)
}

// deserialize takes a string representation of a binary tree,
// converts it back into a binary tree, and returns the root node.
func deserialize(s string) *treeNode {
	if len(s) == 0 {
		return nil
	}

	nodeVals := strings.Split(s, ",")
	return deserializeHelper(nodeVals)
}

// deserializeHelper takes a slice of node values of a binary tree,
// converts it back into a binary tree and returns the root node.
func deserializeHelper(nodeVals []string) *treeNode {
	if len(nodeVals) == 0 {
		return nil
	}

	val := nodeVals[0]
	copy(nodeVals, nodeVals[1:])

	if val == "end" {
		return nil
	}

	root := &treeNode{
		val:   val,
		left:  deserializeHelper(nodeVals),
		right: deserializeHelper(nodeVals),
	}

	return root
}
