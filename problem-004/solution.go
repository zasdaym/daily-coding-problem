package problem004

// lowestMissingPositive returns the lowest missing positive number in given numbers.
func lowestMissingPositive(nums []int) int {
	nums = append(nums, 0)
	n := len(nums)

	// remove invalid numbers
	for i := 0; i < n; i++ {
		if nums[i] < 0 || nums[i] >= n {
			nums[i] = 0
		}
	}

	// tricky part, because all numbers inside the slice now < n,
	// then every number % n will be the number itself.
	// We can use this to turn the given slice like "map".
	// How? By using the slice index as key like in map.
	// Every time we found a number, add nums[num%n] with n,
	// so in the end every number frequency will be nums[i] / n.
	// Shortly, the num % n trick works because all numbers >= n has been removed before.
	for i := 0; i < n; i++ {
		nums[nums[i]%n] += n
	}

	// find number with 0 frequency
	for i := 1; i < n; i++ {
		if nums[i]/n == 0 {
			return i
		}
	}
	return n
}
