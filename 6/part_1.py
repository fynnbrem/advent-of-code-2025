"""Task: https://adventofcode.com/2025/day/6"""
from util import do_chain_math
from typing import Literal


def read_data(path: str) -> list[tuple[list[int], Literal["*", "+"]]]:
    """Reads the data.

    :returns: Every column of the data. Each item is:
        1. The numbers of the column.
        2. The operator of the column."""
    slices = list()
    rows = open(path).read().split("\n")

    # We know that the last row has the operators.
    number_rows = len(rows) - 1
    symbol_row = rows[number_rows]

    # First we must separate the columns.
    # For this, we use the operator row to find out where each column ends.
    start = None
    for index, char in enumerate(symbol_row):
        if char != " ":
            if start is not None:
                slices.append(slice(start, index))
            start = index

    slices.append(slice(start, None))

    # Then we use these slices to read out the numbers of each column row-by-row.
    columns = list()

    for slice_ in slices:
        column = list()
        for row in rows[:number_rows]:
            column.append(int(row[slice_]))
        operation = (rows[number_rows][slice_].strip())

        columns.append((column, operation))

    return columns


DATA = read_data("data.txt")


def main():
    """Calculates the result of each column according to cephalopod math."""
    total_sum = 0
    for numbers, operator in DATA:
        total_sum += do_chain_math(numbers, operator)

    print("Grand total of all calculations:", total_sum)


if __name__ == '__main__':
    main()  # 6299564383938
