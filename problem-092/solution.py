from typing import Dict, List, Set


def courses_to_take(course_to_prereqs: Dict[str, Set[str]]) -> Set[str]:
    # get courses without prereq
    todos: List[str] = [course for course, prereqs in course_to_prereqs.items()
                        if not prereqs]

    # build prereq to courses dict
    prereq_to_courses: Dict[str, Set[str]] = {}
    for course in course_to_prereqs:
        for prereq in course_to_prereqs[course]:
            # prereq without any prereq (basic course)
            if prereq not in prereq_to_courses:
                prereq_to_courses[prereq]: Set[str] = set()

            prereq_to_courses[prereq].add(course)

    result: List[str] = []

    while todos:
        prereq = todos.pop()
        result.append(prereq)

        # find next course to be accomplished with current course
        for course in prereq_to_courses.get(prereq, []):
            course_to_prereqs[course].remove(prereq)
            if not course_to_prereqs[course]:
                todos.append(course)

    print(prereq_to_courses)
    # circluar dependency
    if len(result) < len(course_to_prereqs):
        return []

    return result


course_to_prereqs_test = {
    "CSC300": {"CSC100", "CSC200"},
    "CSC200": {"CSC100"},
    "CSC100": {},
}

print(courses_to_take(course_to_prereqs_test))
