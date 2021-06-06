package problem097

// multiTimeMap is a collection of timeMaps.
type multiTimeMap struct {
	timeMaps map[int]*timeMap
}

// newMultiTimeMap creates a new multiTimeMap.
func newMultiTimeMap() *multiTimeMap {
	m := &multiTimeMap{
		timeMaps: make(map[int]*timeMap),
	}
	return m
}

// get gets most recent value of a key relative to given time.
func (m *multiTimeMap) get(key, time int) int {
	tm := m.timeMaps[key]
	if tm == nil {
		return -1
	}
	return tm.get(time)
}

// set sets a value of a key on specific time.
func (m *multiTimeMap) set(key, val, time int) {
	if _, ok := m.timeMaps[key]; !ok {
		m.timeMaps[key] = &timeMap{}
	}
	m.timeMaps[key].set(time, val)
}

// timeMap is a map that can retrieve the value of a key at a particular time.
type timeMap struct {
	keys   []int
	values []int
}

// set sets a value given time as key
func (tm *timeMap) set(key, val int) {
	if tm.keys == nil {
		tm.keys = append(tm.keys, key)
		tm.values = append(tm.values, val)
	}

	i := getNearestKey(tm.keys, key)
	if tm.keys[i] == key {
		tm.values[i] = val
	} else {
		insert(tm.keys, i+1, key)
		insert(tm.values, i+1, val)
	}
}

// get gets a value at a particular time.
func (tm *timeMap) get(key int) int {
	i := getNearestKey(tm.keys, key)
	if i < 0 {
		return -1
	}

	return tm.values[i]
}

// getNearestKey returns the index of the nearest time key.
func getNearestKey(nums []int, key int) int {
	pos := -1
	for i, num := range nums {
		if num <= key {
			pos = i
		}
	}
	return pos
}

// insert inserts value to given int slice at given index
func insert(nums []int, index, value int) {
	if len(nums) == index {
		nums = append(nums, value)
	}
	nums = append(nums[:index+1], nums[index:]...)
	nums[index] = value
}
