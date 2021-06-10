package problem007

import "strconv"

func decodeWays(msg string) int {
	if len(msg) == 0 {
		return 1
	}

	if len(msg) <= 2 {
		num, _ := strconv.Atoi(msg)
		if num < 10 || num > 26 {
			return 1
		} else {
			return 2
		}
	}

	// ways to decode with first char stripped
	singlePrefixResult := decodeWays(msg[1:])

	// check if remaining message has only single way to decode
	remainingNum, _ := strconv.Atoi(msg[2:])
	if remainingNum > 26 {
		return singlePrefixResult
	}

	// ways to decode with two first chars stripped
	doublePrefixresult := decodeWays(msg[2:])

	return singlePrefixResult + doublePrefixresult
}
