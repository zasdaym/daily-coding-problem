from typing import List
import random

def pick(stream: List[int]) -> int:
    result: int = None
    for index, element in enumerate(stream):
        if index == 0 or random.randint(1, index+1) == 1:
            result = element
    return result
