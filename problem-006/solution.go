package linkedlist

import (
	"unsafe"
)

type node struct {
	value     int
	adjacency *node
}

type xorLinkedList struct {
	head *node
	tail *node
}

func (l *xorLinkedList) add(element int) {
	n := node{value: element, adjacency: l.tail}
	if l.head == nil {
		l.head, l.tail = &n, &n
		return
	}
	l.tail.adjacency = xorNodeAddr(l.tail.adjacency, &n)
	l.tail = &n
}

func (l *xorLinkedList) get(index int) int {
	prevNode := (*node)(nil)
	currentNode := l.head
	for i := 0; i < index; i++ {
		nextNode := xorNodeAddr(currentNode.adjacency, prevNode)
		prevNode = currentNode
		currentNode = nextNode
	}
	return currentNode.value
}

func xorNodeAddr(first *node, second *node) *node {
	return (*node)(unsafe.Pointer(uintptr(unsafe.Pointer(first)) ^ uintptr(unsafe.Pointer(second))))
}
