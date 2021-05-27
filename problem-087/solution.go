package problem087

import "strings"

type direction string

const (
	N  direction = "N"
	NE direction = "NE"
	E  direction = "E"
	SE direction = "SE"
	S  direction = "S"
	SW direction = "SW"
	W  direction = "W"
	NW direction = "NW"
)

// coordinate represent a coordinate in euclidean geometry.
type coordinate struct {
	x, y int
}

// deltas contains relative delta for each direction.
var deltas = map[direction]coordinate{
	N:  {0, -1},
	NE: {1, -1},
	E:  {1, 0},
	SE: {1, 1},
	S:  {1, 0},
	SW: {-1, 1},
	W:  {0, -1},
	NW: {-1, -1},
}

// isValidRules checks if given rules are valid.
func isValidRules(rules []string) bool {
	coordinates := make(map[string]coordinate)
	for _, rule := range rules {
		parts := strings.Split(rule, " ")
		dstName, dir, srcName := parts[0], direction(parts[1]), parts[2]
		dst, dstFound := coordinates[dstName]
		src, srcFound := coordinates[srcName]
		delta := deltas[dir]

		switch {
		case srcFound && dstFound:
			if !isValidRule(src, dst, dir) {
				return false
			}
		case dstFound && !srcFound:
			coordinates[srcName] = coordinate{dst.x - delta.x, dst.y - delta.y}
		case !dstFound && srcFound:
			coordinates[dstName] = coordinate{src.x + delta.x, dst.y + delta.y}
		default:
			coordinates[srcName] = coordinate{0, 0}
			coordinates[dstName] = coordinate{delta.x, delta.y}
		}
	}
	return true
}

func isValidRule(src, dst coordinate, dir direction) bool {
	switch dir {
	case N:
		return isOver(src, dst)
	case NE:
		return isOver(src, dst) && isOnRight(src, dst)
	case E:
		return isOnRight(src, dst)
	case SE:
		return isUnder(src, dst) && isOnRight(src, dst)
	case S:
		return isUnder(src, dst)
	case SW:
		return isUnder(src, dst) && isOnLeft(src, dst)
	case W:
		return isOnLeft(src, dst)
	case NW:
		return isOver(src, dst) && isOnLeft(src, dst)
	default:
		return false
	}
}

func isOver(src, dst coordinate) bool {
	return dst.y < src.y
}

func isUnder(src, dst coordinate) bool {
	return dst.y > src.y
}

func isOnLeft(src, dst coordinate) bool {
	return dst.x < src.x
}

func isOnRight(src, dst coordinate) bool {
	return dst.x > src.x
}
