package problem113

import "testing"

func TestReverseWords(t *testing.T) {
	testCases := []struct {
		name     string
		s        string
		expected string
	}{
		{
			name:     "empty string",
			s:        "",
			expected: "",
		},
		{
			name:     "3 words",
			s:        "hello world here",
			expected: "here world hello",
		},
		{
			name:     "4 words",
			s:        "hello world down here",
			expected: "here down world hello",
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := reverseWords(tc.s)
			if tc.expected != got {
				t.Errorf("want %s got %s", tc.expected, got)
			}
		})
	}
}
