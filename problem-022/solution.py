from typing import List


def reconstruct_string(words: List[str], target: str) -> List[str]:
    """
    Create two index left and right to keep substring range.
    For every substring, check if it exists on the dict.
    If exists, append the substring to result and move the left index to the right index.
    """
    left, right = 0, 0
    result: List[str] = []
    while right <= len(target):
        if target[left:right] in words:
            result.append(target[left:right])
            left = right
        right += 1
    return result


assert reconstruct_string(["quick", "brown", "the", "fox"], "thequickbrownfox") == [
    "the", "quick", "brown", "fox"]

assert reconstruct_string(["bed", "bath", "bedbath", "and", "beyond"], "bedbathandbeyond") == [
    "bed", "bath", "and", "beyond"]
