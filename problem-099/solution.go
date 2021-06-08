package problem099

type bound struct {
	left, right int
}

func longestConsecutiveLength(nums []int) int {
	maxLen := 0
	bounds := make(map[int]bound)

	for _, num := range nums {
		// number already visited
		if _, ok := bounds[num]; ok {
			continue
		}

		leftBound, rightBound := num, num

		// left neighbor exists
		if _, ok := bounds[num-1]; ok {
			leftBound = bounds[num-1].left
		}

		// right neighbor exists
		if _, ok := bounds[num+1]; ok {
			rightBound = bounds[num+1].right
		}

		// update bounds
		newBound := bound{left: leftBound, right: rightBound}
		bounds[num] = newBound
		bounds[leftBound] = newBound
		bounds[rightBound] = newBound

		// update result
		newLen := rightBound - leftBound + 1
		if newLen > maxLen {
			maxLen = newLen
		}
	}

	return maxLen
}
