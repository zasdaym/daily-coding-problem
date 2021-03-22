from typing import List, Tuple

def get_minimum_classroom(lectures: List[Tuple[int, int]]):
    """
    Sort the lecture list by their start time.
    Create a list of rooms.
    For every class check every room if it can reuse the room.
    If cannot reuse a room, append a new one to the list.
    """
    lectures.sort()
    rooms = []
    for lecture in lectures:
        need_new_room = True
        for i, room in enumerate(rooms):
            if lecture[1] < room[0] or lecture[0] > room[1]:
                rooms[i] = lecture
                need_new_room = False
                break
        if need_new_room:
            rooms.append(lecture)
    return len(rooms)

assert get_minimum_classroom([(0, 50), (30, 75), (60, 150), (10, 30)]) == 3