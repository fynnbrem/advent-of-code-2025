"""Task: https://adventofcode.com/2025/day/7"""
from util import Grid

DATA = Grid.from_text(open("data.txt").read())

START = (DATA.data[0].index("S"), 0)

SPLITTER = "^"
TRAVERSED = "|"


def traverse(grid: Grid[str], start: tuple[int, int]) -> int:
    """Recursively traverse the grid, starting on `start` and going downwards.
    Will split on splitters and return the number of splits along the full path.
    Paths that already were traversed will not be traversed again."""
    # Mark the current cell as already traversed.
    grid[start] = TRAVERSED

    next_pos = grid.get_dir(start, "s")
    splits = 0

    # Check if the next position exists (vertical border) or if it already has been traversed.
    if next_pos is not None and grid[next_pos] != TRAVERSED:
        if grid[next_pos] == SPLITTER:
            splits += 1
            left = grid.get_dir(next_pos, "w")
            right = grid.get_dir(next_pos, "e")

            # Check if the neighbouring positions exist (horizontal border) or if they already have been traversed.
            if left is not None and grid[left] != TRAVERSED:
                splits += traverse(grid, left)
            if right is not None and grid[right] != TRAVERSED:
                splits += traverse(grid, right)
        else:
            splits += traverse(grid, next_pos)

    return splits


def main():
    """Traverse the grid with the beam, starting on the "S" start."""
    splits = traverse(DATA, START)
    print("Total beam splits:", splits)


if __name__ == '__main__':
    main()
