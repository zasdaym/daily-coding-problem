import random


def estimate_pi():
    """
    Estimate pi with Monte Carlo Method.
    The main logic is circle area = pi * r^2. And square area = (2r)^2 = 4r^2.
    So, circle area / square area = pi / 4.
    Based on this, the method is to randomly create a point, and track of count whether it is inside the circle or not using pythagoras theorem.
    """
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


print(estimate_pi())
