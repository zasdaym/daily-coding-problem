from typing import List
from random import randint


def shuffle_deck(deck: List[int]) -> None:
    """
    This is called Fisher-Yates algorithm.
    1. Iterate from the back of the array, index as i.
        1. Generate a random integer j where 0 <= j <= i.
        2. Swap arr[i] and arr[j]
    """
    last_index = len(deck) - 1
    for i in range(last_index, 0, -1):
        j = randint(0, i+1)
        deck[i], deck[j] = deck[j], deck[i]


original_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_deck = original_deck.copy()
shuffle_deck(test_deck)
assert original_deck != test_deck
