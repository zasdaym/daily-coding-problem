package problem117

import "container/list"

type treeNode struct {
	val         int
	left, right *treeNode
}

type queue struct {
	l *list.List
}

type queueItem struct {
	node  *treeNode
	level int
}

func newQueue() *queue {
	l := list.New()
	q := &queue{
		l: l,
	}
	return q
}

func (q *queue) push(node *treeNode, level int) {
	item := queueItem{node: node, level: level}
	q.l.PushBack(item)
}

func (q *queue) pop() (node *treeNode, level int) {
	e := q.l.Front()
	q.l.Remove(e)
	item := e.Value.(queueItem)
	return item.node, item.level
}

func (q *queue) isEmpty() bool {
	return q.l.Len() == 0
}

func minLevelSum(root *treeNode) int {
	if root == nil {
		return 0
	}

	nodeQueue := newQueue()
	nodeQueue.push(root, 0)
	sumByLevel := make(map[int]int)

	for !nodeQueue.isEmpty() {
		currNode, currLevel := nodeQueue.pop()
		sumByLevel[currLevel] += currNode.val

		if currNode.left != nil {
			nodeQueue.push(currNode.left, currLevel+1)
		}

		if currNode.right != nil {
			nodeQueue.push(currNode.right, currLevel+1)
		}
	}

	minLevel, minSum := 0, sumByLevel[0]
	for level, sum := range sumByLevel {
		if sum < minSum {
			minSum = sum
			minLevel = level
		}
	}

	return minLevel
}
