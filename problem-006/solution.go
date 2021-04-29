package problem006

import (
	"fmt"
	"unsafe"
)

// node represent a binary tree node.
type node struct {
	value     int
	neighbour *node
}

// xorLinkedList represent a XOR based double linked list.
type xorLinkedList struct {
	head      *node
	tail      *node
	nodeCount int
}

// Add a node into a XOR based double linked list.
func (l *xorLinkedList) Add(element int) {
	n := node{value: element, neighbour: l.tail}
	if l.head == nil {
		l.head, l.tail = &n, &n
	} else {
		l.tail.neighbour = xorNodeAddr(l.tail.neighbour, &n)
		l.tail = &n
	}
	l.nodeCount++
}

// Get node value on specific index on a XOR based double linked list.
func (l *xorLinkedList) Get(index int) (int, error) {
	if index > l.nodeCount-1 {
		return 0, fmt.Errorf("index out out range")
	}
	prevNode := (*node)(nil)
	currentNode := l.head
	for index > 0 {
		nextNode := xorNodeAddr(currentNode.neighbour, prevNode)
		prevNode = currentNode
		currentNode = nextNode
		index--
	}
	return currentNode.value, nil
}

// xorNodeAddr unsafely XOR two Node address.
func xorNodeAddr(first *node, second *node) *node {
	return (*node)(unsafe.Pointer(uintptr(unsafe.Pointer(first)) ^ uintptr(unsafe.Pointer(second))))
}
