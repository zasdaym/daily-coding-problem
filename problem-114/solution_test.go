package problem114

import "testing"

func TestReverse(t *testing.T) {
	testCases := []struct {
		name      string
		s         string
		delimiter string
		expected  string
	}{
		{
			name:      "empty string",
			s:         "",
			delimiter: "/:",
			expected:  "",
		},
		{
			name:      "delimiter in the middle",
			s:         "hello:world/here",
			delimiter: "/:",
			expected:  "here:world/hello",
		},
		{
			name:      "delimiter in the end",
			s:         "hello:world/here/",
			delimiter: "/:",
			expected:  "here:world/hello/",
		},
		{
			name:      "double delimiter",
			s:         "hello::world/here/",
			delimiter: "/:",
			expected:  "here::world/hello/",
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := reverse(tc.s, tc.delimiter)
			if tc.expected != got {
				t.Errorf("want %s got %s", tc.expected, got)
			}
		})
	}
}
