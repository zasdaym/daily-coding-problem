package problem097

import "testing"

func TestMultiTimeMap(t *testing.T) {
	m := newMultiTimeMap()
	m.set(1, 1, 0)
	m.set(1, 1, 2)

	if m.get(1, -12) != -1 {
		t.Errorf("want %v got %v", -1, m.get(1, -12))
	}

	if m.get(1, 1) != 1 {
		t.Errorf("want %v got %v", 1, m.get(1, 1))
	}

	if m.get(1, 3) != 1 {
		t.Errorf("want %v got %v", 2, m.get(1, 1))
	}
}
