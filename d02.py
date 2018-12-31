# Advent of Code 2018 Day 2
# Matthew Hawkins


def main():
    with open("input02.txt") as file:
        box_string_array = file.readlines()

    # Part 1
    double_count = 0
    triple_count = 0

    for box in box_string_array:
        letter_counts = [box.count(c) for c in box]
        if 2 in letter_counts:
            double_count += 1
        if 3 in letter_counts:
            triple_count += 1
    print(double_count * triple_count)

    # Part 2
    for index, box1 in enumerate(box_string_array):
        for box2 in box_string_array[index:]:
            diff_char_index = set()
            for char_index, char in enumerate(box1):
                if box2[char_index] != char:
                    diff_char_index.add(char_index)
                if len(diff_char_index) > 1:
                    break
            if len(diff_char_index) == 1:
                ind = diff_char_index.pop()
                return print(box1[:ind] + box1[ind+1:])


if __name__ == "__main__":
    main()
