// Package linkedlist implements linked list data structure.
package linkedlist

import (
	"fmt"
	"unsafe"
)

// Node represent a binary tree node.
type Node struct {
	value     int
	neighbour *Node
}

// XORLinkedList represent a XOR based double linked list.
type XORLinkedList struct {
	head      *Node
	tail      *Node
	nodeCount int
}

// Add a node into a XOR based double linked list.
func (l *XORLinkedList) Add(element int) {
	n := Node{value: element, neighbour: l.tail}
	if l.head == nil {
		l.head, l.tail = &n, &n
	} else {
		l.tail.neighbour = xorNodeAddr(l.tail.neighbour, &n)
		l.tail = &n
	}
	l.nodeCount++
}

// Get node value on specific index on a XOR based double linked list.
func (l *XORLinkedList) Get(index int) (int, error) {
	if index > l.nodeCount-1 {
		return 0, fmt.Errorf("index out out range")
	}
	prevNode := (*Node)(nil)
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
func xorNodeAddr(first *Node, second *Node) *Node {
	return (*Node)(unsafe.Pointer(uintptr(unsafe.Pointer(first)) ^ uintptr(unsafe.Pointer(second))))
}
