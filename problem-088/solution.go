package problem088

// division implements division without division, multiplication, and modulus operator.
func division(dividend, divisor int) int {
	sign := 1
	if (dividend < 0 && divisor > 0) || (dividend > 0 && divisor < 0) {
		sign = -1
	}

	dividend = abs(dividend)
	divisor = abs(divisor)

	quotient := 0
	for dividend > divisor {
		dividend -= divisor
		quotient++
	}

	return sign * quotient
}

func abs(n int) int {
	if n < 0 {
		n *= -1
	}
	return n
}
