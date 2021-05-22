package problem001

// twoSum checks the existence of pair in given numbers where the sum is equal to the target.
func twoSum(nums []int, target int) bool {
	seen := make(map[int]bool)
	for _, num := range nums {
		if seen[target-num] {
			return true
		}
		seen[num] = true
	}
	return false
}
