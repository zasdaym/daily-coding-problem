package problem095

func nextPermutation(nums []int) {
	pivot := len(nums) - 2

	for pivot >= 0 && nums[pivot] >= nums[pivot+1] {
		pivot--
	}

	if pivot >= 0 {
		successor := len(nums) - 1
		for successor > 0 && nums[successor] <= nums[pivot] {
			successor--
		}
		nums[pivot], nums[successor] = nums[successor], nums[pivot]
	}

	reverse(nums, pivot+1, len(nums)-1)
}

func reverse(nums []int, start, end int) {
	for start < end {
		nums[start], nums[end] = nums[end], nums[start]
		start++
		end--
	}
}
