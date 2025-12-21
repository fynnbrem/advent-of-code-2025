"""Task: https://adventofcode.com/2025/day/9"""
from shared import read_data

DATA = read_data("data.txt")


def main() -> None:
    """Calculate the size of the largest possible rectangle."""
    sizes = list()
    for index_a, pos_a in enumerate(DATA):
        for pos_b in DATA[index_a + 1:]:
            sizes.append(get_rect_size(pos_a, pos_b))

    sizes = sorted(sizes)
    print("Largest rectangle:", sizes[-1])


def get_rect_size(pos_a: tuple[int, int], pos_b: tuple[int, int]):
    """Calculate the sizes of the rectangle that spans from `pos_a` to `pos_b`."""
    # We must add 1 to each side's length as the positions have a size of 1 themselves.
    return (abs(pos_b[0] - pos_a[0]) + 1) * (abs(pos_b[1] - pos_a[1]) + 1)


if __name__ == '__main__':
    main()
