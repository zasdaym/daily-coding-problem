package problem090

import (
	"testing"
)

func TestRandExcept(t *testing.T) {
	t.Run("all possible values in exception", func(t *testing.T) {
		n, exclusion, repeat := 5, []int{0, 1, 2, 3, 4, 5}, 10
		for i := 0; i < repeat; i++ {
			if got := randExcept(n, exclusion); got != -1 {
				t.Errorf("want %v got %v", -1, got)
			}
		}
	})

	t.Run("possible values exists", func(t *testing.T) {
		n, exclustion, repeat := 10, []int{3, 6, 1}, 10
		results := make(map[int]int)
		for i := 0; i < repeat; i++ {
			result := randExcept(n, exclustion)
			results[result]++
			if results[result] > 5 {
				t.Error("not random enough, 50% result is same")
			}
		}
	})
}
