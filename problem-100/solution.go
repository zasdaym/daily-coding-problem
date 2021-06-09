package problem100

// point represents a point in a 2d grid system
type point struct {
	x, y int
}

// coverPoints calculates steps to be taken to cover all given points.
func coverPoints(points []point) int {
	total := 0
	for i := 0; i < len(points)-1; i++ {
		dist := getDistance(points[i], points[i+1])
		total += dist
	}
	return total
}

// getDistance calculates minimum distance between two points.
func getDistance(src, dst point) int {
	xDist := src.x - dst.x
	if xDist < 1 {
		xDist *= -1
	}

	yDist := src.y - dst.y
	if yDist < 1 {
		yDist *= -1
	}

	if xDist > yDist {
		return xDist
	} else {
		return yDist
	}
}
