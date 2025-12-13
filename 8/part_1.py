"""Task: https://adventofcode.com/2025/day/8"""
import math

from shared import read_data, Pos, merge_circuit

MAX_CONNECTIONS, DATA = read_data("data.txt")

TOP_N = 3


def main() -> None:
    """Connects all boxes to a single circuit."""

    # First we calculate all distances between any box.
    distances = list()
    for index_a, box_a in enumerate(DATA):
        # We don't need the distances from the box to itself or flipped positions, so skip these pairs.
        for box_b in DATA[index_a + 1:]:
            distance = math.dist(box_a, box_b)
            distances.append(((box_a, box_b), distance))

    # Then we form the circuits.
    circuits = form_connections(distances, MAX_CONNECTIONS)
    sizes = [len(c) for c in circuits]
    sizes = sorted(sizes, reverse=True)

    print(f"Product of top {TOP_N} circuits:", math.prod(sizes[:TOP_N]))


def form_connections(distances: list[tuple[tuple[Pos, Pos], float]], max_connections: int) -> list[set[Pos]]:
    """Forms connections between the boxes until we tried to form a connection `max_connections` times,
    always connecting the closest two boxes.

    :returns: The generated circuits. Only includes circuits with at least two boxes."""

    distances = sorted(distances, key=lambda x: x[1])
    circuits: list[set[Pos]] = list()

    for (box_a, box_b), _ in distances[:max_connections]:
        circuit_a = get_circuit(box_a, circuits)
        circuit_b = get_circuit(box_b, circuits)

        if circuit_a is None and circuit_b is None:
            # If both boxes are free, we form a new circuit from both.
            circuits.append({box_a, box_b})
        elif circuit_a is None:
            # If only box A is free, we add it to box B's circuit.
            circuits[circuit_b].add(box_a)
        elif circuit_b is None:
            # If only box B is free, we add it to box A's circuit.
            circuits[circuit_a].add(box_b)
        elif circuit_a != circuit_b:
            # If both boxes are part of a different circuit, we merge both into one.
            merge_circuit(circuits, circuit_a, circuit_b)
        # If both boxes are part of the same circuit, nothing happens.

    return circuits


def get_circuit(box: Pos, circuits: list[set[Pos]]) -> int | None:
    """Finds the circuit the `box` is in. Returns `None` if it is not yet connected to any circuit."""
    for index, circuit in enumerate(circuits):
        if box in circuit:
            return index
    return None


if __name__ == '__main__':
    main()  # 50760
