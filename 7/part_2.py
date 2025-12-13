"""Task: https://adventofcode.com/2025/day/7#part2"""
from util import Grid

DATA = Grid.from_text(open("data.txt").read())

START = (DATA.data[0].index("S"), 0)

SPLITTER = "^"

CACHE = dict()


def traverse(grid: Grid[str], start: tuple[int, int]) -> int:
    """Recursively traverse the grid, starting on `start` and going downwards.
    Will split on splitters and return the number of splits along the full path."""

    # Check if we already encountered this position, in which case we can just take the cached value.
    if start in CACHE:
        return CACHE[start]

    next_pos = grid.get_dir(start, "s")
    splits = 0

    # Check if the next position exists (vertical border).
    if next_pos is not None and grid[next_pos]:
        if grid[next_pos] == SPLITTER:
            splits += 1
            left = grid.get_dir(next_pos, "w")
            right = grid.get_dir(next_pos, "e")

            # Check if the neighbouring positions exist (horizontal border).
            if left is not None and grid[left]:
                splits += traverse(grid, left)
            if right is not None and grid[right]:
                splits += traverse(grid, right)
        else:
            splits += traverse(grid, next_pos)

    CACHE[start] = splits
    return splits


def main():
    """Traverse the grid with the beam, starting on the "S" start."""
    splits = traverse(DATA, START)
    print("Total beam splits:", splits + 1)


if __name__ == '__main__':
    main()
