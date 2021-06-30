package problem120

// Service represents a dummy singleton service.
type Service struct {
	val int
}

// Global represents a global context in which singletons exist.
type Global struct {
	even, odd *Service
	calls     int
}

// New creates a new global context.
func New() *Global {
	return &Global{
		even: &Service{1},
		odd:  &Service{2},
	}
}

// GetInstance returns one of two possible singletons.
func (g *Global) GetInstance() *Service {
	g.calls++
	if g.calls%2 == 1 {
		return g.odd
	} else {
		return g.even
	}
}
