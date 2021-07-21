package problem140

import "testing"

func TestSingleElements(t *testing.T) {
	testCases := []struct {
		nums           []int
		firstExpected  int
		secondExpected int
	}{
		{
			nums:           []int{2, 4, 6, 10, 8, 10, 2, 6},
			firstExpected:  4,
			secondExpected: 8,
		},
	}

	for _, tc := range testCases {
		first, second := singleElements(tc.nums)
		if tc.firstExpected != first {
			t.Errorf("Want %d got %d", tc.firstExpected, first)
		}
		if tc.secondExpected != second {
			t.Errorf("want %d got %d", tc.secondExpected, second)
		}
	}
}
