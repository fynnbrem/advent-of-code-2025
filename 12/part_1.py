"""Task: https://adventofcode.com/2025/day/12"""
import re

MAX_PRESENT_SIZE = 9


# ↑ The size a present would have if all its slots were occupied.

def read_data(path: str):
    """Reads the data from the `path`.

    :returns:
        1. The presents (Only their sizes).
        2. The trees, each item is:
            1. The dimensions of the area below the tree.
            2. The count of presents (index wise) required for the tree."""
    text = open(path).read()

    # Read and format the presents.
    presents_str: list[str] = re.findall(r"(?<=\d:\n).*?(?=\n\n)", text, flags=re.DOTALL)

    presents = list()
    for present in presents_str:
        # We only need the size and not the actual shape down the line.
        presents.append(present.count("#"))

    # Read and format the trees.
    trees_str: list[str] = re.findall(r"\d+x\d+:.*$", text, flags=re.MULTILINE)

    trees = list()
    for tree in trees_str:
        area_str, config_str = tree.split(":")
        area = tuple(int(x) for x in area_str.split("x"))
        config = [int(x) for x in config_str.strip().split(" ")]
        trees.append((area, config))

    return presents, trees


def main() -> None:
    """Calculate the amount of trees for which all presents will fit."""
    presents, trees = read_data("data.txt")
    fit_sum = 0
    for area, config in trees:
        if will_fit(presents, area, config):
            fit_sum += 1

    print("Trees with all presents:", fit_sum)


def will_fit(presents: list[int], area: tuple[int, int], config: list[int]) -> bool:
    """Check if the `presents` in the given `config` would fit in the `area`."""
    # This function makes some generous assumptions about the data, but it works.

    # Calculate the minimum and maximum size that the presents would occupy.
    min_size = sum(presents[i] * config[i] for i in range(len(config)))
    max_size = sum(config) * MAX_PRESENT_SIZE
    area_size = area[0] * area[1]

    print(presents, area, config)
    print(min_size, max_size, area_size)

    if area_size < min_size:
        # If the area is too small to fit the presents even if they were perfectly packed, this cannot fit.
        return False

    if area_size >= max_size:
        # If the area is large enough for all presents to fit even in the worst configuration,
        # this will most likely fit.
        return True

    # We cannot assume a full fit or full non-fit, so we would need to simulate it.
    # We don't do that and just hope this case never applies.
    raise ValueError("Cannot calculate fit.")


if __name__ == '__main__':
    main()
