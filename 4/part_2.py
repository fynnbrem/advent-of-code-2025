"""Task: https://adventofcode.com/2025/day/4#part2"""
from util import Grid

DATA = Grid.from_text(open("data.txt").read())


def main():
    """Iterate over every cell of the grid and check if the spot is valid for pickup."""
    valid_spots = 0

    # `1` to enter the loop the first time.
    new_spots = 1
    while new_spots > 0:
        # We keep depleting the map of spots until we get one iteration where 0 new valid spots were found.
        # This means the map was not modified, and we can assume we found all valid spots.
        new_spots = 0

        for cell in DATA.iter_cells():
            nbors = DATA.get_neighbours(*cell)
            if DATA.get(*cell) == "@":
                # The neighbours function gives us all neighbours,
                # so we just need to count that we have less than 4 occupied spots and our current spot is occupied.
                occupied_nbors = nbors.count("@")
                if occupied_nbors < 4:
                    valid_spots += 1
                    new_spots += 1
                    DATA.set(*cell, ".")

    print("Valid loading spots:", valid_spots)


if __name__ == '__main__':
    main()  # 8765
