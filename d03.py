# Advent of Code 2018 Day 3
# Matthew Hawkins


from itertools import chain


class Claim:

    def __init__(self, i, l, t, w, h):
        self.id_num = int(i)
        self.left_indent = int(l)
        self.top_indent = int(t)
        self.width = int(w)
        self.height = int(h)


class ClaimCounts:

    def __init__(self, w, h):
        self.counts = [[0 for n in range(w)] for n in range(h)]

    def increment(self, x, y):
        self.counts[x][y] += 1

    def claim_overlaps(self, claim):
        for x in range(claim.left_indent, claim.left_indent + claim.width):
            for y in range(claim.top_indent, claim.top_indent + claim.height):
                if self.counts[x][y] > 1:
                    return True
        return False


def main():
    with open("puzzleInputs/03.txt") as file:
        claim_string_array = file.readlines()

    claims = []
    for claim_string in claim_string_array:
        asplit = claim_string[1:].split("@")
        csplit = asplit[1].split(":")

        id_num = int(asplit[0].strip())
        li, ti = csplit[0].strip().split(",")
        w, h = csplit[1].strip().split("x")

        claims.insert(id_num, Claim(id_num, li, ti, w, h))

    max_width = max(c.left_indent + c.width for c in claims)
    max_height = max(c.top_indent + c.height for c in claims)
    claim_counts = ClaimCounts(max_width, max_height)

    # Part 1
    for claim in claims:
        for x in range(claim.left_indent, claim.left_indent + claim.width):
            for y in range(claim.top_indent, claim.top_indent + claim.height):
                claim_counts.increment(x, y)
    print(sum([claim_count > 1 for claim_count in chain.from_iterable(claim_counts.counts)]))

    # Part 2
    for claim in claims:
        if not claim_counts.claim_overlaps(claim):
            return print(claim.id_num)


if __name__ == "__main__":
    main()
