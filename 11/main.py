"""Task: https://adventofcode.com/2025/day/11 (part 1 and part 2)

This code assumes that the graph is non-cyclic."""


def read_data(path: str) -> dict[str, list[str]]:
    """Reads the data.
    :returns:
        The graph. The keys are the source node, the values the nodes that the source node links to."""

    rows = open(path).read().split("\n")
    graph = dict()
    for row in rows:
        source, targets = row.split(":")
        targets = [t for t in targets.strip().split(" ")]
        graph[source] = targets

    return graph


DATA = read_data("data.txt")

YOU = "you"
SVR = "svr"
OUT = "out"

DAC = "dac"
FFT = "fft"

CACHE: dict[tuple[str, str], int] = dict()


def traverse(node: str, graph: dict[str, list[str]], end: str) -> int:
    """Traverse the `graph`, starting on the `node`.
    :returns:
        The count of paths that end on the `end` node."""

    if (node, end) in CACHE:
        return CACHE[(node, end)]

    paths = 0

    next_nodes = graph[node]
    # For every node branching from this node, we check if it has special properties.
    for next_node in next_nodes:
        # Check if we hit the desired terminating node.
        if next_node == end:
            paths += 1
            continue
        # Check if we reached the end without hitting the terminating node (in which case the path does not count).
        elif next_node == OUT:
            continue

        paths += traverse(next_node, graph, end)

    CACHE[(node, end)] = paths
    return paths


def main() -> None:
    """Count all connections:
        * From "you" to "out" (part 1)
        * from "svr" to "out" over "fft" and "dac" (part 2)
    """

    # Part 1
    # We just need to find every path from "you" to "out".
    you_to_out = traverse(YOU, DATA, OUT)
    print('Paths from "you" to "out":', you_to_out)  # 699

    # Part 2
    # We need to guarantee, that "fft" and "dac" are part of the path.
    # To do this, we split the paths in segments separated by "svr" and "dac".
    # This way, we know which paths will lead there without having to retroactively check for them.

    # We need to check "fft" -> "dac" as well as "dac" -> "fft" even though only one can exist in non-cyclic graphs,
    # so we can work with any dataset.
    allowed_routes = [
        [SVR, DAC, FFT, OUT],
        [SVR, FFT, DAC, OUT],
    ]

    total_paths = 0
    for route in allowed_routes:

        # To get the actual path count for every route,
        # we get the path count of every segment and permutate it with the next by multiplying it.
        local_total_paths = 1
        for index in range(len(route) - 1):
            new_paths = traverse(route[index], DATA, route[index + 1])
            local_total_paths = local_total_paths * new_paths

        total_paths += local_total_paths

    print('Paths from "svr" to "out" over "fft" and "dac":', total_paths)  # 388893655378800


if __name__ == '__main__':
    main()
