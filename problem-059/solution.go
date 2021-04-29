package problem059

import "fmt"

type file []byte

type rsync struct {
	files   []file
	targets []*rsync
}

func (r *rsync) addTarget(t *rsync) {
	r.targets = append(r.targets, t)
}

func (r *rsync) addFile(f file) int {
	r.files = append(r.files, f)
	for _, t := range r.targets {
		t.sendAddFile(f)
	}
	return len(r.files) - 1
}

func (r *rsync) updateFile(id int, f file) error {
	if id < 0 || id >= len(r.files) {
		return fmt.Errorf("invalid file id")
	}

	for _, t := range r.targets {
		t.sendUpdateFile(id, f)
	}
	return nil
}

func (r *rsync) deleteFile(id int) error {
	if id < 0 || id >= len(r.files) {
		return fmt.Errorf("invalid file id")
	}
	r.files[id] = nil
	for _, t := range r.targets {
		t.sendDeleteFile(id)
	}
	return nil
}

func (r *rsync) getFile(id int) file {
	if id < 0 || id >= len(r.files) {
		return nil
	}
	return r.files[id]
}

func (r *rsync) sendAddFile(f file) {
	r.addFile(f)
}

func (r *rsync) sendDeleteFile(id int) {
	r.deleteFile(id)
}

func (r *rsync) sendUpdateFile(id int, f file) {
	for i, b := range f {
		if i >= len(r.files[id]) {
			r.files[id] = append(r.files[id], b)
		}
		if r.files[id][i] != b {
			r.sendByte(id, i, b)
		}
	}
	r.files[id] = r.files[id][:len(f)]
}

func (r *rsync) sendByte(id, index int, b byte) {
	r.files[id][index] = b
}
