package problem009

func maxNonAdjacentSum(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	if len(nums) == 1 {
		return nums[0]
	}

	if len(nums) == 2 {
		return max(nums[0], nums[1])
	}

	exclusive, inclusive := 0, nums[0]
	for _, num := range nums[1:] {
		exclusive, inclusive = inclusive, max(inclusive, exclusive+num)
	}
	return max(inclusive, exclusive)
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
