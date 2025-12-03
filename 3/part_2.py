"""Task: https://adventofcode.com/2025/day/3#part2"""
DATA = open("data.txt").read().split("\n")


def get_largest_digit(number: str):
    """Returns the index of the largest digit of the `number`. For equal digits, a lower index is preferred."""
    pairs = [(x, i) for i, x in enumerate(number)]
    pairs = sorted(pairs, reverse=True, key=lambda pair: (pair[0], -pair[1]))
    return pairs[0][1]


def main():
    """Finds the largest joltage for every row of batteries."""
    total_sum = 0

    for num in DATA:
        # We find the largest joltage without checking every possible combination.
        # For this, we use that for the largest joltage, the highest digit must always be first.
        # So we first get the highest digit,
        # and then check for the highest digit that is in the tail after the previous highest digit,
        # until we got all 12 digits.
        # We also make sure there are always enough digits left to form a full 12-digit
        # number by limiting the range for each search.
        digit_indexes = list()

        for index in range(11, -1, -1):
            # Limit the search range to start only after the previous digit
            # and stop so there are always enough digits left to form a full 12-digit number.
            if len(digit_indexes) == 0:
                start = 0
            else:
                start = digit_indexes[-1] + 1

            stop = len(num) - index

            largest = get_largest_digit(num[start:stop]) + start
            digit_indexes.append(largest)

        merged = "".join(num[i] for i in digit_indexes)

        total_sum += int(merged)

    print("Sum of all maximum Joltage:", total_sum)


if __name__ == '__main__':
    main()  # 168798209663590
