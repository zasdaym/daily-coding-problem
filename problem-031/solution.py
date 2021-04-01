from typing import Dict, Tuple


def min_edit_distance(a: str, b: str) -> int:
    """
    Call recursive helper function to find the minimum edit distance
    between two string.
    """
    return __min_edit_distance(a, b, dict())


def __min_edit_distance(a: str, b: str, cache: Dict[Tuple[str, str]]) -> int:
    """
    Known as Levenshtein distance.
    Iterate from left to right using recursion while checking for
    insertion, deletion, or substitution possibilities.
    The insertion, deletion, and substituion logic better explained in the code directly.
    Return the minimum distance between the insertion, deletion, or substitution.
    Also use cache to avoid recompute computed solution.
    """
    if not a and not b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    if a[0] == b[0]:
        return min_edit_distance(a[1:], b[1:])
    if (a, b) not in cache:
        insertion = 1 + min_edit_distance(a, b[1:])
        deletion = 1 + min_edit_distance(a[1:], b)
        substitution = 1 + min_edit_distance(a[1:], b[1:])
        cache[(a, b)] = min(insertion, deletion, substitution)
    return cache[(a, b)]


assert min_edit_distance("kitten", "sitting") == 3
