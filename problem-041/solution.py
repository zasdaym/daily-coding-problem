from typing import List, Tuple


def get_itinerary(flights: List[Tuple[str, str]], itinerary: List[str]) -> List[str]:
    """
    A backtracking solution (try every solution and move on immediately from a branch if condititon unmet).
    1. Sort flights information.
    2. Try to add every flight to itinerary, then recursively check if there is any valid next flight.
    3. When there is no next flight found, remove the inserted flight from the itinerary.
    """
    flights.sort()

    if not flights:
        return itinerary

    last_stop = itinerary[-1]
    for i, (origin, destination) in enumerate(flights):
        remaining_flights = flights[:i] + flights[i+1:]
        itinerary.append(destination)
        if last_stop == origin:
            return get_itinerary(remaining_flights, itinerary)
        itinerary.pop()
    return None


assert get_itinerary([("A", "B"), ("A", "C"), ("B", "X"),
                      ("B", "C"), ("C", "A"), ("C", "B")], ["A"]) == ["A", "B", "C", "A", "C", "B", "X"]

assert get_itinerary([("SFO", "HKO"), ("YYZ", "SFO"), ("YUL", "YYZ"), ("HKO", "ORD")], ["YUL"]) == [
    "YUL", "YYZ", "SFO", "HKO", "ORD"]
