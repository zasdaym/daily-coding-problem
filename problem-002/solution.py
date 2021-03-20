from typing import List
import math


def arr_product(numbers: List[int]) -> List[int]:
    product = math.prod(numbers)
    result = [product/number for number in numbers]
    return result


assert arr_product([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert arr_product([3, 2, 1]) == [2, 3, 6]
