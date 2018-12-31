# Advent of Code 2018 Day 8
# Matthew Hawkins


from collections import defaultdict


numbers_p1 = []
numbers_p2 = []


def main():
    global numbers_p1
    global numbers_p2
    with open("input08.txt") as file:
        inp = file.readline().split()

    parsed_input = [int(num) for num in inp]
    numbers_p1 = parsed_input.copy()
    numbers_p2 = parsed_input.copy()
    print(parse_child_p1())
    print(parse_child_p2())


# Part 1
def parse_child_p1():

    global numbers_p1
    node = numbers_p1[:2]
    numbers_p1 = numbers_p1[2:]
    meta = 0

    for child in range(node[0]):
        meta += parse_child_p1()
    meta += sum(numbers_p1[:node[1]])
    numbers_p1 = numbers_p1[node[1]:]
    return meta


# Part 2
def parse_child_p2():

    global numbers_p2
    node = numbers_p2[:2]
    numbers_p2 = numbers_p2[2:]
    meta = 0

    if node[0] > 0:
        children = defaultdict(int)
        for child in range(1, node[0]+1):
            children[child] = parse_child_p2()

        meta_children = numbers_p2[:node[1]]
        for child in meta_children:
            meta += children[child]
    else:
        meta = sum(numbers_p2[:node[1]])
    numbers_p2 = numbers_p2[node[1]:]
    return meta


if __name__ == "__main__":
    main()
