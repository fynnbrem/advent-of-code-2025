DATA = open("data.txt", "r").read().split("\n")

INITIAL_POS = 50
MAX_POS = 100


def turn_dial(start, instruction) -> tuple[int, int]:
    """Turn the dial with the `start` position as defined by the `instruction`.
    :returns:
        (<The new position>, <The amount of zero-passes>)"""
    direction, steps = instruction[0], int(instruction[1:])

    if steps == 0:
        return start, 1

    # First we trim out the full rotations and directly translate them to zero-passes.
    full_rotations = steps // MAX_POS
    partial_rotation = steps % MAX_POS

    zero_passes = full_rotations

    # Then we apply the remaining rotation to the current position.
    if direction == "L":
        partial_rotation = -partial_rotation
    new_pos = (start + partial_rotation) % MAX_POS

    # Then we derive the zero-passes from the new state.
    # Be aware that this uses only the non-full-rotation rest.
    if start != 0 and new_pos == 0:
        # If we stop on 0, we have a zero-pass.
        zero_passes += 1
    elif direction == "L" and new_pos > start != 0:
        # If the value rises despite a left-rotation, we had a zero-pass.
        # This only applies if we did not start at 0, as this would not be a pass.
        zero_passes += 1
    elif direction == "R" and new_pos < start:
        # If the value drops despite a right-rotation, we had a zero-pass.
        zero_passes += 1

    return new_pos, zero_passes


def main() -> None:
    """Turn the dial with every instruction from the data."""
    pos = 50
    zero_count = 0
    for instruction in DATA:
        start_pos = pos
        pos, new_zero_passes = turn_dial(start_pos, instruction)
        zero_count += new_zero_passes

    print("Count of zero-passes:", zero_count)


if __name__ == '__main__':
    main()
