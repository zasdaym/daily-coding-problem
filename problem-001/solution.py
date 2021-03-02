def two_sum(numbers, target):
    visited = {}
    for number in numbers:
        diff = target - number
        if diff in visited:
            return True
        visited[number] = True
    return False

assert two_sum([10, 15, 3, 7], 17)
assert two_sum([1, 2, 3, 4], 4)
assert not two_sum([], 12)
assert not two_sum([1, 2, 3, 4], 12)
