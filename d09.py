from collections import defaultdict, deque

def main():
    with open("puzzleInputs/09.txt") as file:
        inp = file.readline().split()
    number_of_players = int(inp[0])
    last_marble_value = int(inp[-2])
    print(getHighScore(number_of_players, last_marble_value))
    print(getHighScore(number_of_players, last_marble_value * 100))


def getHighScore(number_of_players, last_marble_value):
    scores = defaultdict(int)
    marbles = deque([0])

    for marble_value in range(1, last_marble_value):
        if marble_value % 23 == 0:
            marbles.rotate(7)
            scores[marble_value % number_of_players] += marble_value + marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(marble_value)
    return max(scores.values())


if __name__ == "__main__":
    main()
