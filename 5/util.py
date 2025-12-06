def read_data(path: str) -> tuple[list[tuple[int, int]], list[int]]:
    """Reads the data from the `path`.
    :returns:
        1. The list of ranges.
        2. The list of IDs."""

    text = open(path).read()
    ranges, numbers = text.split("\n\n")

    ranges_int = [range_str_to_int(r) for r in ranges.split("\n")]
    numbers_int = [int(n) for n in numbers.split("\n")]

    return ranges_int, numbers_int


def range_str_to_int(range_str: str) -> tuple[int, int]:
    """Converts a range represented as string to a proper tuple of integers."""
    start, stop = range_str.split("-")
    return (int(start), int(stop))
