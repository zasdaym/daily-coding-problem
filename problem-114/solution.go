package problem114

import (
	"fmt"
	"regexp"
	"strings"
)

func reverse(s string, delimiters string) string {
	// Get words
	delimiterRegex := regexp.MustCompile(fmt.Sprintf("[%s]+", delimiters))
	words := delimiterRegex.Split(s, -1)

	// Get delimiters
	nonDelimiterRegex := regexp.MustCompile(fmt.Sprintf("[^(%s)]+", delimiters))
	nonWords := nonDelimiterRegex.Split(s, -1)

	var result strings.Builder

	// Check if last word is empty (when there is a delimiter in the end)
	wordPos := len(words) - 1
	if words[wordPos] == "" {
		wordPos--
	}

	// Combine reversed words and the delimiters
	for _, delimiter := range nonWords {
		result.WriteString(delimiter)
		if wordPos < 0 {
			continue
		}
		result.WriteString(words[wordPos])
		wordPos--
	}

	return result.String()
}
