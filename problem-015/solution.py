from typing import List
import random


def pick(stream: List[int]) -> int:
    """
    Reservoir sampling technique.
    Simply decrease the probability for every iteration to create uniform probability for all elements. 

    """
    result: int = None
    for index, element in enumerate(stream):
        if random.randint(1, index+1) == 1:
            result = element
    return result

result = pick([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(result)