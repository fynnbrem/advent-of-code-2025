type Pos = tuple[int, int, int]


def read_data(path: str) -> tuple[int, list[Pos]]:
    """Reads the data from the `path`.
    :returns:
        1. The maximum connections intended for the data.
        2. The positions of the boxes."""
    max_connections, positions = open(path).read().split("\n\n")
    rows = positions.split("\n")

    return int(max_connections), [tuple(int(c) for c in row.split(",")) for row in rows]


def merge_circuit(circuits: list[set[Pos]], index_a: int, index_b: int) -> None:
    """Merges the circuits at the two indexes into one. The merged circuit will be at `index_a`.
    Modifies `circuits` in-place."""
    circuits[index_a].update(circuits[index_b])
    circuits.pop(index_b)
