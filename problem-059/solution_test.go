package problem059

import (
	"reflect"
	"testing"
)

func TestRsync(t *testing.T) {
	f1 := file("abcdefg")
	f2 := file("xyz123")

	src := &rsync{}
	target := &rsync{}

	src.addTarget(target)
	src.addFile(f1)
	src.addFile(f2)

	f1Updated := file("abczefg")
	src.updateFile(0, f1Updated)
	if f := target.getFile(0); !reflect.DeepEqual(f, f1Updated) {
		t.Errorf("f1 doesn't match inside the target: %v, %v", f, f1Updated)
	}

	f2Updated := file("bbbbbb")
	src.updateFile(1, f2Updated)
	if f := target.getFile(1); !reflect.DeepEqual(f, f2Updated) {
		t.Errorf("f2 doesn't match inside the target: %v, %v", f, f2Updated)
	}

	if target.getFile(100) != nil {
		t.Errorf("expect nil but got file")
	}

	if err := src.deleteFile(0); err != nil {
		t.Errorf("error deleting file: %w", err)
	}

	if target.getFile(0) != nil {
		t.Errorf("file not deleted")
	}
}
