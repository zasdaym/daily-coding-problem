package problem082

import (
	"strings"
	"testing"
)

func TestRead7(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		reads    int
		expected []string
	}{
		{
			name:     "Hello world",
			input:    "Hello world",
			reads:    3,
			expected: []string{"Hello w", "orld", ""},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			r := strings.NewReader(tc.input)
			for i := 0; i < tc.reads; i++ {
				got := read7(r)
				if tc.expected[i] != got {
					t.Errorf("want %s got %s", tc.expected[i], got)
				}
			}
		})
	}
}

func TestReadN(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		n        int
		reads    int
		expected []string
	}{
		{
			name:     "read7 3 times",
			input:    "Hello world",
			n:        7,
			reads:    3,
			expected: []string{"Hello w", "orld", ""},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			r := strings.NewReader(tc.input)
			for i := 0; i < tc.reads; i++ {
				got := readN(r, tc.n)
				if tc.expected[i] != got {
					t.Errorf("want %s got %s", tc.expected[i], got)
				}
			}
		})
	}
}
