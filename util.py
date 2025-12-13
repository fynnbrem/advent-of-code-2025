from typing import Iterable, Generic, TypeVar, Generator, Literal

T = TypeVar("T")

type Pos = tuple[int, int]


class Grid(Generic[T]):
    """A grid. Can represent 2D dimensional data."""

    def __init__(self, data: Iterable[Iterable[T]]):
        # Cast the data to be a list.
        self.data = [list(row) for row in data]
        assert all(len(row) == len(self.data[0]) for row in self.data[1:]), "All rows must have the same length"
        self.dim = (len(self.data[0]), len(self.data))

    @classmethod
    def from_text(cls, text: str) -> "Grid[str]":
        """Create this class from a block of `text`.
        Every row of text is converted to a grid row, every character to a single cell."""
        return cls(text.split("\n"))

    def get(self, x: int, y: int) -> T:
        """Return the cell value at column `x` and row `y`."""
        return self.data[y][x]

    def set(self, x: int, y: int, value: T) -> None:
        """Set the cell value at column `x` and row `y`."""
        self.data[y][x] = value

    def __getitem__(self, pos: Pos) -> T:
        return self.get(*pos)

    def __setitem__(self, pos: Pos, value: T) -> None:
        self.set(*pos, value)

    def get_neighbours(self, x: int, y: int) -> list[Pos]:
        """Returns all neighbours of the cell at `(x, y)`. Includes diagonals.
        The cells are returned in clockwise order, starting at 12 o'clock."""
        coords = [
            (x, y - 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
            (x, y + 1),
            (x - 1, y + 1),
            (x - 1, y),
            (x - 1, y - 1)
        ]

        return [self.get(*coord) for coord in coords if self.is_in_bounds(*coord)]

    def iter_cells(self) -> Generator[Pos, None, None]:
        """Iterate over all cells in this grid.
        Returns their positions, going through columns first."""
        return ((x, y) for y, row in enumerate(self.data) for x, _ in enumerate(row))

    def is_in_bounds(self, x: int, y: int) -> bool:
        """Check if `(x, y)` is an index within the boundaries of this grid."""
        return 0 <= x < self.dim[0] and 0 <= y < self.dim[1]

    def as_text(self) -> str:
        """Format the grid as string by merging the rows to text lines."""
        return "\n".join(("".join(row) for row in self.data))

    def print(self):
        """Prints the grid as string by merging the rows to text lines."""
        print(self.as_text())

    def get_dir(self, pos: Pos, direction: Literal["n", "e", "s", "w"]) -> Pos | None:
        """Return the coordinates of the cell in the `direction` from the `pos`.
        Returns `None` if it would be out of bounds."""

        match direction:
            case "n":
                new = (pos[0], pos[1] - 1)
            case "e":
                new = (pos[0] + 1, pos[1])
            case "s":
                new = (pos[0], pos[1] + 1)
            case "w":
                new = (pos[0] - 1, pos[1])
            case _:
                raise ValueError("Invalid direction.")

        if self.is_in_bounds(*new):
            return new
        else:
            return None


if __name__ == "__main__":
    grid = Grid.from_text("123\n456\n789")
    print(grid.data)
    print(grid.get_neighbours(1, 1))
    print(list(grid.iter_cells()))
