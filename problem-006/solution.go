package linkedlist

import (
	"fmt"
	"unsafe"
)

type Node struct {
	value     int
	neighbour *Node
}

type XORLinkedList struct {
	head      *Node
	tail      *Node
	nodeCount int
}

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

func xorNodeAddr(first *Node, second *Node) *Node {
	return (*Node)(unsafe.Pointer(uintptr(unsafe.Pointer(first)) ^ uintptr(unsafe.Pointer(second))))
}
