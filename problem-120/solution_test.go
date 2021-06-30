package problem120

import "testing"

func TestGetInstance(t *testing.T) {
	g := New()
	first := g.GetInstance()
	second := g.GetInstance()
	if first == second {
		t.Errorf("first and second instance should not be identical")
	}
	for i := 0; i < 100; i++ {
		if first != g.GetInstance() {
			t.Errorf("wrong instance given on odd call")
		}
		if second != g.GetInstance() {
			t.Errorf("wrong instance given on even call")
		}
	}
}
