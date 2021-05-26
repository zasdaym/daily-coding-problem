package problem005

type pairFunc func(x, y int) int
type pairFuncExecutor func(f pairFunc) int

func cons(a, b int) pairFuncExecutor {
	pair := func(f pairFunc) int {
		return f(a, b)
	}
	return pair
}

func car(f pairFuncExecutor) int {
	return f(func(x, y int) int {
		return x
	})
}

func cdr(f pairFuncExecutor) int {
	return f(func(x, y int) int {
		return y
	})
}
