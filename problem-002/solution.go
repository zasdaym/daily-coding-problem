package problem002

// exclusiveProducts returns new slice of integers
// such that each element at index i of the new slice
// is the product of all the numbers in the original slice
// excluding the one at index i. Implemented without division.
func exclusiveProducts(nums []int) []int {
	result := make([]int, len(nums))
	if len(nums) < 2 {
		return result
	}

	leftCumulative := make([]int, len(nums))
	leftCumulative[0] = nums[0]

	rightCumulative := make([]int, len(nums))
	rightCumulative[len(nums)-1] = nums[len(nums)-1]

	for i := 1; i < len(nums); i++ {
		leftCumulative[i] = leftCumulative[i-1] * nums[i]
		rightIndex := len(nums) - i - 1
		rightCumulative[rightIndex] = rightCumulative[rightIndex+1] * nums[rightIndex]
	}

	result[0] = rightCumulative[1]
	result[len(nums)-1] = leftCumulative[len(nums)-2]
	for i := 1; i < len(nums)-1; i++ {
		result[i] = leftCumulative[i-1] * rightCumulative[i+1]
	}

	return result
}
