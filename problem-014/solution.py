import random


def estimate_pi():
    circle_points = 0
    square_points = 0
    result = 0

    while square_points < 1000:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if (x**2 + y**2) <= 1:
            circle_points += 1
        square_points += 1

        result = 4 * circle_points / square_points
    return result


print(estimate_p())
