package problem113

import "strings"

// reverseWords reverses given string of space separated words and return the reversed order of the words.
func reverseWords(s string) string {
	words := strings.Split(s, " ")

	left, right := 0, len(words)-1
	for left < right {
		words[left], words[right] = words[right], words[left]
		left++
		right--
	}

	return strings.Join(words, " ")
}
