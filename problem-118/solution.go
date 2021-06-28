package problem118

import "sort"

func sortSquared(nums []int) []int {
	var squaredNums []int
	for _, num := range nums {
		squaredNums = append(squaredNums, num*num)
	}

	sort.Ints(squaredNums)
	return squaredNums
}
