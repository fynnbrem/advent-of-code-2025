"""Task: https://adventofcode.com/2025/day/5"""
from util import read_data

DATA = read_data("data.txt")


def is_in_range(number, range):
    """Check if `number` is in `range` (both ends inclusive)."""
    return range[0] <= number <= range[1]


def main():
    """Check for every number, if it is in any range."""
    numbers_in_range = 0

    ranges, numbers = DATA
    for number in numbers:
        for range_ in ranges:
            if is_in_range(number, range_):
                numbers_in_range += 1
                # Every number must only be counted once if it is valid.
                break

    print("Fresh ingredients:", numbers_in_range)


if __name__ == "__main__":
    main()
