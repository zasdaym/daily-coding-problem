package linkedlist

import (
	"testing"
)

func TestXORLinkedList(t *testing.T) {
	linkedList := &XORLinkedList{}
	for i := 0; i <= 10; i++ {
		linkedList.Add(i)
	}

	t.Run("get on correct index", func(t *testing.T) {
		want := 6
		get, err := linkedList.Get(want)
		if err != nil {
			t.Errorf("failed to get node at index %d: %w", want, err)
		}
		if get != want {
			t.Errorf("want %d, got %d", want, get)
		}
	})

	t.Run("get on wrong index", func(t *testing.T) {
		_, err := linkedList.Get(100)
		if err == nil {
			t.Errorf("want err, got nil")
		}
	})
}
