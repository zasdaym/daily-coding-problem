from typing import List


def sort_rgb(rgbs: List[int]) -> None:
    """
    This can be solved using two approaches.
    Counting sort is easy, but only element swapping is alloed.
    The other approaches is the three segment sort.

    Create three pointers, two on the front and one on the end of the array.
    First pointer is to iterating the array (curr).
    Second pointer is for 1/3 of the array (red).
    Third pointer is for 3/3 of the array (blue).
    Iterate from the front, until curr bypass the blue pointer.
    If current char is "R", replace the content on "red" with "curr", and move "red" forward.
    If current char is "B", replace the content on "blue" with "curr", and move "blue" backward.
    """
    curr = 0
    red = 0
    blue = len(rgbs) - 1

    while curr <= blue:
        if rgbs[curr] == "R":
            rgbs[curr], rgbs[red] = rgbs[red], rgbs[curr]
            red += 1
        elif rgbs[curr] == "B":
            rgbs[curr], rgbs[blue] = rgbs[blue], rgbs[curr]
            blue -= 1
        curr += 1


colors = ["B", "G", "R", "R", "B", "G", "G", "R"]
sort_rgb(colors)
assert colors == ["R", "R", "R", "G", "G", "G", "B", "B"]
