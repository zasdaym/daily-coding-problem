from typing import Dict, List, Tuple

deltas: Dict[str, Tuple[int, int]] = {
    "N": (0, -1),
    "NE": (1, -1),
    "E": (1, 0),
    "SE": (1, 1),
    "S": (0, 1),
    "SW": (-1, 1),
    "W": (-1, 0),
    "NW": (-1, -1)
}


def is_valid_rules(rules: List[str]) -> bool:
    coordinates: Dict[str, Tuple[int, int]] = {}

    for rule in rules:
        part = rule.split(" ")
        src, dst, direction = part[2], part[0], part[1]

        src_exists: bool = src in coordinates
        dst_exists: bool = dst in coordinates
        delta = deltas[direction]

        if src_exists and dst_exists:
            if not is_valid_rule(coordinates[src], coordinates[dst], direction):
                return False
        elif src_exists:
            coordinates[dst] = (coordinates[src][0] + delta[0], coordinates[src][1] + delta[1])
        elif dst_exists:
            coordinates[src] = (coordinates[dst][0] - delta[0], coordinates[dst][1] - delta[1])
        else:
            coordinates[src] = (0, 0)
            coordinates[dst] = delta
        
    return True


def is_valid_rule(src: Tuple[int, int], dst: Tuple[int, int], direction: str) -> bool:
    if direction == "N":
        return is_over(src, dst)
    elif direction == "NE":
        return is_over(src, dst) and is_on_right(src, dst)
    elif direction == "E":
        return is_on_right(src, dst)
    elif direction == "SE":
        return is_under(src, dst) and is_on_right(src, dst)
    elif direction == "S":
        return is_under(src, dst)
    elif direction == "SW":
        return is_under(src, dst) and is_on_left(src, dst)
    elif direction == "W":
        return is_on_left(src, dst)
    elif direction == "NW":
        return is_over(src, dst) and is_on_right(src, dst)
    else:
        return False

def is_over(src: Tuple[int, int], dst: Tuple[int, int]) -> bool:
    return dst[1] < src[1]

def is_under(src: Tuple[int, int], dst: Tuple[int, int]) -> bool:
    return dst[1] > src[1]

def is_on_left(src: Tuple[int, int], dst: Tuple[int, int]) -> bool:
    return dst[0] < src[0]

def is_on_right(src: Tuple[int, int], dst: Tuple[int, int]) -> bool:
    return dst[0] > src[1]