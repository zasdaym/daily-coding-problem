package problem140

// singleElements returns two elements that appear exactly once in given slice of integers.
func singleElements(nums []int) (int, int) {
	// If we XOR all numbers in the slice, duplicate numbers will cancel each other, because A XOR A is 0.
	// Then we left with the XOR of two unique numbers.
	uniqueNumsXOR := 0
	for _, num := range nums {
		uniqueNumsXOR ^= num
	}

	// Get rightmost set bit (bit that is 1), call this position i.
	uniqueNumsXOR = uniqueNumsXOR & -uniqueNumsXOR

	// Next we need to get the two numbers from the XOR.
	// We separate the given slice into two groups, numbers with i-th bit set and numbers with i-th bit off.
	// XOR all numbers in each group, and we got the two unique numbers.
	first, second := 0, 0
	for _, num := range nums {
		if uniqueNumsXOR&num != 0 {
			first ^= num
		} else {
			second ^= num
		}
	}
	return first, second
}
