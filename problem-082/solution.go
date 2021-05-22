package problem082

import "io"

// read7 reads only 7 bytes (or lower) at a time from given io.Reader.
func read7(r io.Reader) string {
	lr := &io.LimitedReader{
		R: r,
		N: 7,
	}

	b := make([]byte, 7)
	n, err := lr.Read(b)
	if err != nil {
		return ""
	}
	return string(b[:n])
}

// readN reads N-bytes using only the read7 function that reads 7 bytes (or lower) at a time.
func readN(r io.Reader, n int) string {
	result := make([]byte, n)
	readBytesCount := 0
	for readBytesCount < n {
		readBytes := read7(r)
		if len(readBytes) == 0 {
			break
		}
		copy(result[readBytesCount:], []byte(readBytes))
		readBytesCount += len(readBytes)
	}
	return string(result[:readBytesCount])
}
