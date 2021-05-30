package problem090

import (
	"math/rand"
)

// randExcept generate random number from 0 to n excluding number in given slice.
func randExcept(n int, exclusion []int) int {
	excludes := make(map[int]bool)
	for _, num := range exclusion {
		excludes[num] = true
	}

	candidates := make([]int, 0)
	for i := 0; i <= n; i++ {
		if excludes[i] {
			continue
		}
		candidates = append(candidates, i)
	}

	if len(candidates) == 0 {
		return -1
	}

	result := candidates[rand.Intn(len(candidates)-1)]
	return result
}
