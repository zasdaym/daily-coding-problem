package problem088

import "testing"

func TestDivision(t *testing.T) {
	testCases := []struct {
		name     string
		dividend int
		divisor  int
		expected int
	}{
		{
			name:     "both positive",
			dividend: 10,
			divisor:  3,
			expected: 3,
		},
		{
			name:     "both negative",
			dividend: -15,
			divisor:  -8,
			expected: 1,
		},
		{
			name:     "negative and positive",
			dividend: 45,
			divisor:  -8,
			expected: -5,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := division(tc.dividend, tc.divisor)
			if tc.expected != got {
				t.Errorf("want %d got %d", tc.expected, got)
			}
		})
	}
}
