"""Task: https://adventofcode.com/2025/day/6#part2"""
from util import do_chain_math
from typing import Literal


def read_data(path: str) -> list[tuple[list[int], Literal["*", "+"]]]:
    """Reads the data.

    :returns: Every column of the data. Each item is:
        1. The numbers of the column.
        2. The operator of the column."""
    slices = list()
    rows = open(path).read().split("\n")

    # Pad all rows to have the same length so we can more easily work with it down the line.
    max_len = max(len(row) for row in rows)
    rows = [row.ljust(max_len, " ") for row in rows]

    # We know that the last row has the operators.
    number_rows = len(rows) - 1
    symbol_row = rows[number_rows]

    # First we must separate the columns.
    # For this, we use the operator row to find out where each column ends.
    start = None
    for index, char in enumerate(symbol_row):
        if char != " ":
            if start is not None:
                slices.append(slice(start, index - 1))
            start = index

    slices.append(slice(start, None))

    columns = list()

    # Then we use these slices to read out the numbers of each column, according to cephalopod math.
    for slice_ in slices:
        column_str = list()
        for row in rows[:number_rows]:
            column_str.append(row[slice_])
        column_int = read_numbers(column_str)

        operation = rows[number_rows][slice_].strip()

        columns.append((column_int, operation))

    return columns


def read_numbers(column: list[str]) -> list[int]:
    """Reads out the numbers of the `column` according to cephalopod math
    (Each single character column defines a number, read top-to-bottom).
    Assumes all rows have the same length."""
    numbers = list()
    # Get the max length of all rows, which is relevant for the last column where the string cuts off.

    for index in range(len(column[0])):
        number = ""
        for row in column:
            number += row[index]
        numbers.append(int(number))

    # Order doesn't matter with the given operations, but we reverse it to stay true to the fluff.
    return numbers[::-1]


DATA = read_data("data.txt")


def main():
    """Calculates the result of each column according to cephalopod math."""
    total_sum = 0
    for numbers, operation in DATA:
        total_sum += do_chain_math(numbers, operation)

    print("Grand total of all calculations:", total_sum)


if __name__ == '__main__':
    main()  # 11950004808442
