package problem127

import "testing"

func TestSum(t *testing.T) {
	testCases := []struct {
		name     string
		a, b     *listNode
		expected int
	}{
		{
			name: "one empty list",
			a: &listNode{
				val: 3,
				next: &listNode{
					val: 2,
					next: &listNode{
						val: 1,
					},
				},
			},
			b:        nil,
			expected: 123,
		},
		{
			name: "two lists with same length",
			a: &listNode{
				val: 3,
				next: &listNode{
					val: 2,
					next: &listNode{
						val: 1,
					},
				},
			},
			b: &listNode{
				val: 1,
				next: &listNode{
					val: 1,
					next: &listNode{
						val: 5,
					},
				},
			},
			expected: 634,
		},
		{
			name: "two lists with different length",
			a: &listNode{
				val: 3,
				next: &listNode{
					val: 2,
					next: &listNode{
						val: 1,
					},
				},
			},
			b: &listNode{
				val: 1,
				next: &listNode{
					val: 1,
					next: &listNode{
						val: 5,
						next: &listNode{
							val: 2,
						},
					},
				},
			},
			expected: 2634,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			got := sum(tc.a, tc.b)
			if tc.expected != got {
				t.Errorf("want %d got %d", tc.expected, got)
			}
		})
	}
}
