def tower_of_hanoi(n: int, source: str = "A", spare: str = "B", destination: str = "C") -> None:
    """
    The main principle is:
    1. Move n-1 disks from source stack to the spare stack, this leaves the current biggest in the source stack.
    2. Move the disk on the source stack to the final/destination stack.
    3. Move all disks from the spare stack (which we moved from the source stack before) to the final/destination stack.
    """
    if n >= 1:
        tower_of_hanoi(n - 1, source, destination, spare)
        print(f"Move {source} to {destination}")
        tower_of_hanoi(n - 1, spare, source, destination)


tower_of_hanoi(4)
