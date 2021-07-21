package problem138

func minCoins(target int) int {
	coins := []int{25, 10, 5, 1}
	total := 0

	for target > 0 {
		for _, coin := range coins {
			count := target / coin
			target -= count * coin
			total += count
		}
	}

	return total
}
