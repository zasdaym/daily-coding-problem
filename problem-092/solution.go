package problem092

// coursesToTake returns courses to take given course prereqs list.
// Returns empty slice of string when cyclic dependency found.
func coursesToTake(coursePrereqs map[string]map[string]bool) []string {
	// course without any prereq
	todos := make([]string, 0)
	for course, prereqs := range coursePrereqs {
		if len(prereqs) != 0 {
			continue
		}
		todos = append(todos, course)
	}

	// build prereq to course map
	prereqCourses := make(map[string]map[string]bool)
	for course, prereqs := range coursePrereqs {
		for prereq := range prereqs {
			// prevent assigning to nil
			if prereqCourses[prereq] == nil {
				prereqCourses[prereq] = make(map[string]bool)
			}
			prereqCourses[prereq][course] = true
		}
	}

	result := make([]string, 0)
	for len(todos) > 0 {
		prereq := todos[len(todos)-1]
		todos = todos[:len(todos)-1]
		result = append(result, prereq)

		// remove current course from other courses prereqs list
		for course := range prereqCourses[prereq] {
			delete(coursePrereqs[course], prereq)
			if len(coursePrereqs[course]) == 0 {
				todos = append(todos, course)
			}
		}
	}

	// cyclic dependency
	if len(result) < len(coursePrereqs) {
		return []string{}
	}

	return result
}
