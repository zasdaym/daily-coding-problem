package problem007

import "testing"

func TestDecodeWays(t *testing.T) {
	testCases := []struct {
		name     string
		message  string
		expected int
	}{
		{
			name:     "empty message",
			message:  "",
			expected: 1,
		},
		{
			name:     "multi ways decode",
			message:  "111",
			expected: 3,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := decodeWays(tc.message)
			if tc.expected != got {
				t.Errorf("want %v got %v", tc.expected, got)
			}
		})
	}
}
