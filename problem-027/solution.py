from collections import deque

def is_valid_brackets(text: str) -> bool:
    """
    A stack will be used to hold unmatched opener brackets.
    Iterate every char.
    If current char is not a closing bracket, append it to the stack.
    If current char is and closing bracket, pop last element from the stack, and check if the two is pair.
    """
    bracket_pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    unmatched = deque()
    for char in text:
        expected_match = bracket_pairs.get(char, "")
        if expected_match == "":
            unmatched.append(char)
            continue
        
        if not unmatched:
            return False
        last_unmatched = unmatched.pop()
        if expected_match != last_unmatched:
            return False
    
    return len(unmatched) == 0


assert is_valid_brackets("{{[]}}")
assert is_valid_brackets("[]{}([])")
assert not is_valid_brackets("{[]())")