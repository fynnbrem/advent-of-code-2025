"""Task: https://adventofcode.com/2025/day/10"""
import re
from collections import Counter
from itertools import count
from typing import Generator


def read_data(path: str) -> list[tuple[list[bool], list[list[int]], list[int]]]:
    """Read the data from the `path`.

    :returns:
        A list where each machine specification is one item.
        Each item consists of:
            1. The desired light configuration.
            2. The buttons.
            3. The desired joltage configuration."""
    rows = open(path).read().split("\n")

    data = list()
    for row in rows:
        lights_str = re.search(r"\[.*\]", row).group()
        lights = [l == "#" for l in lights_str.strip("[]")]

        buttons_str = re.search(r"\(.*\)", row).group()
        buttons = [[int(b) for b in bs.strip("()").split(",")] for bs in buttons_str.split(" ")]

        joltage_str = re.search(r"\{.*\}", row).group()
        joltage = [int(j) for j in joltage_str.strip("{}").split(",")]

        data.append((lights, buttons, joltage))

    return data


def get_multisets(n: int, k: int) -> Generator[list[int]]:
    """Yields all non-decreasing `k`-tuples of indices in `[0, n-1]`.
    Each tuple represents a multiset combination with repetition.

    :returns:
        A generator where each item is a list of indexes that are picked in the current multiset."""
    combination: list[int] = [0] * k

    while True:
        yield combination

        # Find rightmost position we can increment.
        i = k - 1
        while i >= 0 and combination[i] == n - 1:
            i -= 1
        if i < 0:
            # We incremented every possible position.
            return

        # Increment it.
        combination[i] += 1

        # Set everything to the right equal to combo[i] to keep non-decreasing.
        for j in range(i + 1, k):
            combination[j] = combination[i]


def apply_combination(button_vectors: list[list[int]], combination: list[int], light_count: int) -> list[int]:
    """Apply  the `combination` (A list of button indexes to press) to the `light_count` using the `button_vectors`.

    :returns: The updated light count."""
    presses = Counter(combination)
    lights = [0] * light_count
    for index, press_count in presses.items():
        add_vector(lights, press_count, button_vectors[index])

    return lights


def buttons_to_vectors(buttons: list[list[int]], light_count: int) -> list[list[int]]:
    """Converts button configurations (a list of indexes)
    to a vector (a list of `0` and `1` depending on whether the button contains that index)."""
    return [button_to_vector(b, light_count) for b in buttons]


def button_to_vector(button: list[int], light_count: int) -> list[int]:
    """Converts button configurations (a list of indexes)
    to a vector (a list of `0` and `1` depending on whether the button contains that index)."""
    return [1 if index in button else 0 for index in range(light_count)]


def add_vector(base: list[int], factor: int, vector: list[int]) -> None:
    """Adds `factor * vector` to `base`."""
    for index in range(len(base)):
        base[index] += factor * vector[index]


def main():
    """Finds the least amount of buttons that need to be pressed to get the desired light configuration."""
    data = read_data("data.txt")
    total_sum = 0

    for (lights, buttons, _) in data:
        button_vectors = buttons_to_vectors(buttons, len(lights))

        combination = get_valid_combination(button_vectors, lights)

        # The combination is a list of indexes, so the length is the count of presses.
        total_sum += len(combination)

    print("Sum of all combinations:", total_sum)


def get_valid_combination(button_vectors: list[list[int]], lights: list[bool]):
    """Find the smallest combination of button presses of the `button_vectors` that will result in `lights`."""
    lights_count = len(lights)
    buttons_count = len(button_vectors)

    for press_count in count(1):
        # Create every combination of button presses you can get with the current `press_count`.
        # When we get a valid combination, we return that combination thus getting the smallest possible one.
        for combination in get_multisets(buttons_count, press_count):

            light_switches = apply_combination(button_vectors, combination, lights_count)

            # We calculate the light setup with modulo
            # as we know 2 presses will result in an off-state while 1 press will result in an on-state.
            lights_final = [(ls % 2) == 1 for ls in light_switches]
            if lights_final == lights:
                return combination


if __name__ == '__main__':
    main()
