# Advent of Code 2018 Day 1
# Matthew Hawkins

from itertools import accumulate, cycle


def main():
    with open("puzzleInputs/01.txt") as file:
        int_array = [int(n) for n in file.readlines()]

    # Part 1
    print(sum(int_array))

    # Part 2
    intermediate_total_history = {0}
    for intermediate_total in accumulate(cycle(int_array)):
        if intermediate_total in intermediate_total_history:
            print(intermediate_total)
            break
        intermediate_total_history.add(intermediate_total)


if __name__ == "__main__":
    main()
