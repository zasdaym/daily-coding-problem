package problem092

import (
	"reflect"
	"testing"
)

func TestCoursesToTake(t *testing.T) {
	testCases := []struct {
		name          string
		coursePrereqs map[string]map[string]bool
		expected      []string
	}{
		{
			name:          "empty input",
			coursePrereqs: nil,
			expected:      []string{},
		},
		{
			name: "non circular dependency",
			coursePrereqs: map[string]map[string]bool{
				"CSC300": {
					"CSC200": true,
					"CSC100": true,
				},
				"CSC200": {
					"CSC100": true,
				},
				"CSC100": nil,
			},
			expected: []string{"CSC100", "CSC200", "CSC300"},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := coursesToTake(tc.coursePrereqs)
			if !reflect.DeepEqual(tc.expected, got) {
				t.Errorf("want %v got %v", tc.expected, got)
			}
		})
	}
}
