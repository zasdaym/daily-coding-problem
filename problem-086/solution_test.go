package problem086

import "testing"

func TestMinParanthesesRemove(t *testing.T) {
	testCases := []struct {
		name     string
		s        string
		expected int
	}{
		{
			name:     "empty string",
			s:        "",
			expected: 0,
		},
		{
			name:     "valid simple parantheses",
			s:        "()()()",
			expected: 0,
		},
		{
			name:     "valid nested parantheses",
			s:        "((()()()))",
			expected: 0,
		},
		{
			name:     "unclosed edge parantheses",
			s:        "(()(",
			expected: 2,
		},
		{
			name:     "unclosed middle parantheses",
			s:        "()())()",
			expected: 1,
		},
		{
			name:     "only closing parantheses",
			s:        ")))",
			expected: 3,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := minParanthesesRemove(tc.s)
			if tc.expected != got {
				t.Errorf("want %d got %d", tc.expected, got)
			}
		})
	}
}
