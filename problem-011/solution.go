package problem011

import "strings"

func getPossibleStrings(s string, set []string) []string {
	result := make([]string, 0)
	for _, v := range set {
		if strings.HasPrefix(v, s) {
			result = append(result, v)
		}
	}
	return result
}
