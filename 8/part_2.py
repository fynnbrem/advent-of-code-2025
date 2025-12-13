"""Task: https://adventofcode.com/2025/day/8#part2"""
import math

from shared import read_data, Pos, merge_circuit

MAX_CONNECTIONS, DATA = read_data("data.txt")


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
    last_boxes = form_connections(distances, DATA)
    product = last_boxes[0][0] * last_boxes[1][0]

    print(f"Product of the last 2 boxes:", product)


def form_connections(distances: list[tuple[tuple[Pos, Pos], float]], boxes: list[Pos]):
    """Forms connections between the boxes until they form a single circuit, always connecting the closest two boxes.

    :returns: The last two boxes required to form a single circuit."""
    distances = sorted(distances, key=lambda x: x[1])
    circuits: list[set[Pos]] = [{b} for b in boxes]

    for (box_a, box_b), _ in distances:
        circuit_a = get_circuit(box_a, circuits)
        circuit_b = get_circuit(box_b, circuits)

        if circuit_a != circuit_b:
            # If both boxes are part of a different circuit, we merge both into one.
            merge_circuit(circuits, circuit_a, circuit_b)
            if len(circuits) == 1:
                return box_a, box_b
        # If both boxes are part of the same circuit, nothing happens.

    raise ValueError("Could not merge all circuits into one.")


def get_circuit(box: Pos, circuits: list[set[Pos]]) -> int | None:
    """Finds the circuit the `box` is in."""
    for index, circuit in enumerate(circuits):
        if box in circuit:
            return index
    raise IndexError("The box is not in any circuit.")


if __name__ == '__main__':
    main()  # 3206508875
