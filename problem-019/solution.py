from typing import List
import sys


def get_minimum_painting_cost(cost_matrix: List[List[int]]) -> int:
    """
    Main idea is to keep track of two most minimum cost.
    Because if the most minimum cost on current house is the same color as previous house, we can fallback to second most minimum cost.
    """
    if not cost_matrix:
        return 0

    house_count = len(cost_matrix)
    color_count = len(cost_matrix[0])

    prev_house_min_cost = 0
    prev_house_min_index = -1
    prev_house_second_min_cost = 0

    # Loop for every house
    for i in range(house_count):
        curr_house_min_cost = sys.maxsize
        curr_house_second_min_cost = sys.maxsize
        curr_house_min_index = 0

        # Loop for every color for current house
        for j in range(color_count):
            # If previouse house minimum cost color is same with current color, use second minimum cost instead
            if prev_house_min_index == j:
                cost_matrix[i][j] += prev_house_second_min_cost
            else:
                cost_matrix[i][j] += prev_house_min_cost

            # Check if current cost is minimum
            if curr_house_min_cost > cost_matrix[i][j]:
                curr_house_second_min_cost = curr_house_min_cost
                curr_house_min_cost = cost_matrix[i][j]
                curr_house_min_index = j
            # Check if current cost is second minimum
            elif curr_house_second_min_cost > cost_matrix[i][j]:
                curr_house_second_min_cost = cost_matrix[i][j]

        prev_house_min_cost = curr_house_min_cost
        prev_house_second_min_cost = curr_house_second_min_cost
        prev_house_min_index = curr_house_min_index
        print(prev_house_min_cost, prev_house_second_min_cost)

    return min(cost_matrix[house_count-1])


cost_matrix = [
    [7, 1, 8, 6, 2, 9],
    [5, 6, 1, 4, 4, 2],
    [9, 9, 9, 1, 9, 9]
]
assert get_minimum_painting_cost(cost_matrix) == 5
