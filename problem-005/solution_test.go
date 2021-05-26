package problem005

import "testing"

func TestCar(t *testing.T) {
	want, got := 3, car(cons(3, 4))
	if want != got {
		t.Errorf("want %d got %d", want, got)
	}
}

func TestCdr(t *testing.T) {
	want, got := 4, cdr(cons(3, 4))
	if want != got {
		t.Errorf("want %d got %d", want, got)
	}
}
