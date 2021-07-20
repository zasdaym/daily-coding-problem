package problem138

import "testing"

func TestMinCoins(t *testing.T) {
	testCases := []struct {
		target   int
		expected int
	}{
		{target: 0, expected: 0},
		{target: 16, expected: 3},
		{target: 70, expected: 4},
	}

	for _, tc := range testCases {
		got := minCoins(tc.target)
		if tc.expected != got {
			t.Errorf("want %d got %d", tc.expected, got)
		}
	}
}
