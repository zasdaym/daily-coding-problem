package problem087

import "testing"

func TestIsValidRules(t *testing.T) {
	testCases := []struct {
		name     string
		rules    []string
		expected bool
	}{
		{
			name: "single rule",
			rules: []string{
				"A SW C",
			},
			expected: true,
		},
		{
			name: "invalid rules",
			rules: []string{
				"A N B",
				"B NE C",
				"C N A",
			},
			expected: false,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := isValidRules(tc.rules)
			if tc.expected != got {
				t.Errorf("want %v got %v", tc.expected, got)
			}
		})
	}
}
