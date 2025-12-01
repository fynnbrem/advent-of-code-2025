DATA = open("data.txt", "r").read().split("\n")

INITIAL_POS = 50


def turn_dial(start, instruction):
    """Turn the dial with the `start` position as defined by the `instruction`.
    :returns: The new position."""
    direction, count = instruction[0], int(instruction[1:])
    if direction == "L":
        count = -count

    return ((start + count) % 100)


def main():
    """Turn the dial with every instruction from the data."""
    pos = 50
    zero_count = 0
    for instruction in DATA:
        pos = turn_dial(pos, instruction)
        if pos == 0:
            zero_count += 1

    print("Count of zero-positions:", zero_count)


if __name__ == '__main__':
    main()
