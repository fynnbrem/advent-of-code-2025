DATA = open("data.txt").read().split("\n")


def get_largest_digit(number: str):
    """Returns the index of the largest digit of the `number`. For equal digits, a lower index is preferred."""
    pairs = [(x, i) for i, x in enumerate(number)]

    # We sort by largest digit first, lowest index second by creating a tuple that sorts by that order.
    pairs = sorted(pairs, reverse=True, key=lambda pair: (pair[0], -pair[1]))
    return pairs[0][1]


def main():
    """Finds the largest joltage for every row of batteries."""
    total_sum = 0

    for num in DATA:
        # We find the largest joltage without checking every possible combination.
        # For this, we use that for the largest joltage, the highest digit must always be first.
        # So we first get the highest digit,
        # and then check for the highest digit that is in the tail after that first highest digit.
        # We also make sure there is at least one digit left to be the second digit
        # by limiting the range of the first search.

        # Search initially for the highest digit.
        largest = get_largest_digit(num[:-1])
        # Search again but only in the tail after the first digit.
        second_largest = get_largest_digit(num[largest + 1:]) + largest + 1

        merged = num[largest] + num[second_largest]
        total_sum += int(merged)

    print("Sum of all maximum Joltage:", total_sum)


if __name__ == '__main__':
    main()  # 17034
