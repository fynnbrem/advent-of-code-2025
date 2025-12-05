"""Task: https://adventofcode.com/2025/day/4"""
from util import Grid

DATA = Grid.from_text(open("data.txt").read())


def main():
    """Iterate over every cell of the grid and check if the spot is valid for pickup."""
    valid_spots = 0

    for cell in DATA.iter_cells():
        nbors = DATA.get_neighbours(*cell)
        if DATA.get(*cell) == "@":
            # The neighbours function gives us all neighbours,
            # so we just need to count that we have less than 4 occupied spots and our current spot is occupied.
            occupied_nbors = nbors.count("@")
            if occupied_nbors < 4:
                valid_spots += 1

    print("Valid loading spots:", valid_spots)


if __name__ == '__main__':
    main()  # 1437
