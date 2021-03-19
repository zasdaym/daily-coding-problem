from typing import Dict


def longest_abosolute_path(filesystem: str) -> int:
    """Find length of longest absolute path in the given filesystem string"""
    paths = filesystem.split("\n")
    max_length = 0
    # The main idea is to maintain max length per depth
    max_length_by_depth: Dict[int, int] = {-1: 0}
    for path in paths:
        # Depth is determined by "\t" count
        name = path.strip()
        depth = len(path) - len(name)
        if "." in name:
            max_length = max(
                max_length, max_length_by_depth[depth-1] + len(name))
        else:
            max_length_by_depth[depth] = max_length_by_depth[depth -
                                                             1] + len(name) + 1
    return max_length


filesystem_string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
assert longest_abosolute_path(filesystem_string) == 32
