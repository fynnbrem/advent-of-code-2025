"""Task: https://adventofcode.com/2025/day/2"""
def read_data(path: str) -> list[tuple[int, int]]:
    """Read the data from the `path`.
    :returns: A list of valid ID ranges (both ends inclusive)."""

    sets = open(path, "r").read().split(",")
    as_split = [x.split("-") for x in sets]
    as_int = [(int(x[0]), int(x[1])) for x in as_split]
    return as_int


DATA = read_data("data.txt")


def is_doubling(number: int):
    """Check if the number is the same number repeated twice."""
    as_str = str(number)
    length = len(as_str)
    if length % 2 == 1:
        # Only even numbers can have such pattern.
        return False
    elif as_str[: length // 2] == as_str[length // 2:]:
        # Compare the two halves of the number.
        return True
    else:
        return False


def main():
    """Iterate over every number in the data ranges and check if they are doubling."""
    num_sum = 0
    for start, stop in DATA:
        for x in range(start, stop + 1):
            if is_doubling(x):
                num_sum += x

    print("Sum of Invalid IDs:", num_sum)


if __name__ == '__main__':
    main()  # 32976912643
