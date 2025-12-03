"""Task: https://adventofcode.com/2025/day/2#part2"""
def read_data(path: str) -> list[tuple[int, int]]:
    """Read the data from the `path`.
    :returns: A list of valid ID ranges (both ends inclusive)."""
    sets = open(path, "r").read().split(",")
    as_split = [x.split("-") for x in sets]
    as_int = [(int(x[0]), int(x[1])) for x in as_split]
    return as_int


DATA = read_data("data.txt")
print(DATA)


def is_duplicating(number: int):
    """Check if the number consists only of the same number that is being repeated."""
    as_str = str(number)
    length = len(as_str)
    if length == 1:
        # A single number cannot repeat.
        return False

    # First we get the divisors so we only need to check for bracket sizes that can actually repeat fully.
    divs = get_divisors(length)

    for divisor in divs:
        bracket = length // divisor
        base_slice = as_str[:bracket]
        # Assume the base slice matches with every number,
        # then try to refute it by comparing it with every other slice it must match.
        full_match = True
        for index in range(1, divisor):
            if base_slice != as_str[index * bracket: (index + 1) * bracket]:
                full_match = False

        if full_match:
            return True

    return False


def get_divisors(number: int):
    """Returns all divisors of the `number` (Except `1`)."""
    divs = list()
    for x in range(2, number // 2 + 1):
        if (number / x).is_integer():
            divs.append(x)
    return divs + [number]


def main():
    """Iterate over every number in the data ranges and check if they are duplicating."""
    num_sum = 0
    for start, stop in DATA:
        for x in range(start, stop + 1):
            if is_duplicating(x):
                num_sum += x

    print("Sum of Invalid IDs:", num_sum)


if __name__ == '__main__':
    main()
