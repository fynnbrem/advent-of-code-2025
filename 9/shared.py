def read_data(path: str) -> list[tuple[int, int]]:
    """Reads the data from the `path`.

    :returns: The coordinates of every corner."""


    rows = open(path).read().split("\n")

    return [tuple(int(c) for c in r.split(",")) for r in rows]
