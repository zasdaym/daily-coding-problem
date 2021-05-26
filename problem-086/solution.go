package problem086

func minParanthesesRemove(s string) int {
	if len(s) < 2 {
		return len(s)
	}

	unclosed, invalid := 0, 0

	for _, c := range s {
		if c == '(' {
			unclosed++
		} else if unclosed == 0 {
			invalid++
		} else {
			unclosed--
		}
	}

	return invalid + unclosed
}
