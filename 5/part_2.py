"""Task: https://adventofcode.com/2025/day/5#part2"""
from util import read_data

DATA = read_data("data.txt")


def merge_ranges(first: tuple[int, int], second: tuple[int, int]) -> tuple[int, int]:
    """Merges the two ranges to their maximum extent.
    Assumes that the ranges overlap and the `first` starts before the `second`."""
    start = first[0]
    stop = max(first[1], second[1])
    return start, stop


def is_in_range(number: int, range_: tuple[int, int]) -> bool:
    """Check if the `number` is in the `range_` (both ends inclusive)."""
    return range_[0] <= number <= range_[1]


def do_ranges_overlap(first: tuple[int, int], second: tuple[int, int]) -> bool:
    """Checks if the two ranges overlap (both ends inclusive).
    Assumes that the `first` starts before the `second` (i.e. if anything, the second range starts in the first range)."""

    return is_in_range(second[0], first)


def get_range_sum(ranges: list[tuple[int, int]]) -> int:
    """Calculates the sum of the spans of all `ranges` (Both ends inclusive). Assumes that no ranges overlap."""
    total_sum = 0
    for range_ in ranges:
        total_sum += (range_[1] - range_[0] + 1)

    return total_sum


def main():
    """Determines a list of non-overlapping ranges so we can easily calculate their total sum."""
    ranges, numbers = DATA

    # For more efficient code,
    # we sort the ranges by their start value so we can simplify our code down the line by using that assumption.
    sorted_ranges = sorted(ranges)

    main_index = 0
    # Every iteration, we move one range forward. We try to fit as many of the subsequent ranges as possible
    # by continuously merging them into out current `main_range`.
    while main_index < len(sorted_ranges):
        main_range = sorted_ranges[main_index]
        clear_indexes = list()

        # We must only check ranges after this one because of:
        # * Our sorting.
        # * The completeness of previously created ranges.
        for match_index, match_range in enumerate(sorted_ranges[main_index + 1:]):
            if do_ranges_overlap(main_range, match_range):
                main_range = merge_ranges(main_range, match_range)
                clear_indexes.append(main_index + match_index + 1)

            else:
                # Once we find the first range that does not overlap with the main range,
                # we know there are none left to overlap due to our sorting.
                break

        # Update the main range with the merged value and remove ranges that were merged into it.
        sorted_ranges[main_index] = main_range
        for i in clear_indexes[::-1]:
            sorted_ranges.pop(i)

        main_index += 1

    print("Maximum amount of fresh ingredients:", get_range_sum(sorted_ranges))


if __name__ == '__main__':
    main()
