package problem011

import (
	"reflect"
	"testing"
)

func TestGetPossibleStrings(t *testing.T) {
	testCases := []struct {
		name     string
		s        string
		set      []string
		expected []string
	}{
		{
			name:     "empty string",
			s:        "",
			set:      []string{},
			expected: []string{},
		},
		{
			name:     "some valid matches",
			s:        "de",
			set:      []string{"dog", "deer", "deal"},
			expected: []string{"deer", "deal"},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := getPossibleStrings(tc.s, tc.set)
			if !reflect.DeepEqual(tc.expected, got) {
				t.Errorf("want %v got %v", tc.expected, got)
			}
		})
	}
}
