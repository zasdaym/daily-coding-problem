from typing import List
from unittest import TestCase


def products(nums: List[int]) -> List[int]:
    # Simple solution
    # total_product = 1
    # for num in nums:
    #     total_product *= num
    # return [total_product // num for num in nums]

    # Follow-up without division.
    """
    The result value on i-th element is (product of all element before i) * (product of all element after i).
    So the algorithm is:
    1. Generate prefix_products (All element will hold product of all numbers from start to that index).
    2. Generate suffix_products (All element will hold product of all numbers starting from that index).
    3. Generate result (each element is product of all element before i * product of all element after i)
    """
    prefix_products: List[int] = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    suffix_products: List[int] = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products.reverse()

    result: List[int] = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i+1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i-1])
        else:
            result.append(prefix_products[i-1] * suffix_products[i+1])
    print(prefix_products, suffix_products)
    return result


class TestSolution(TestCase):
    def test(self):
        got = products([1, 2, 3, 4, 5])
        want = [120, 60, 40, 30, 24]
        self.assertEqual(got, want)
