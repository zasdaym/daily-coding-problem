package problem127

type listNode struct {
	val  int
	next *listNode
}

func sum(a, b *listNode) int {
	return listToInt(a) + listToInt(b)
}

func listToInt(head *listNode) int {
	result := 0
	multiplier := 1
	for head != nil {
		result += head.val * multiplier
		multiplier *= 10
		head = head.next
	}
	return result
}
