# Advent of Code 2018 Day 5
# Matthew Hawkins


import re
import sys


def react_polymer(polymer):
    ind = 0
    while ind < len(polymer) - 1:
        if polymer[ind] == polymer[ind + 1].swapcase():
            polymer = polymer[:ind] + polymer[ind + 2:]
            ind = max(0, ind - 1)
        else:
            ind += 1
    return polymer


def main():
    with open("input05.txt") as file:
        initial_polymer = file.readline()

    # Part 1
    print(len(react_polymer(initial_polymer)))

    # Part 2
    min_size = sys.maxsize
    for c in range(65, 91):
        removed_chars = re.compile(chr(c), re.IGNORECASE)
        poly_size = len(react_polymer(removed_chars.sub('', initial_polymer)))
        if poly_size < min_size:
            min_size = poly_size
    print(min_size)


if __name__ == "__main__":
    main()
