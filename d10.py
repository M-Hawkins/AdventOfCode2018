import re
import numpy as np
import matplotlib.pyplot as plt


def main():
    with open("puzzleInputs/10.txt") as file:
        inp = file.readlines()

    positions = []
    velocities = []

    for line in inp:
        values = re.findall(r'\<([^>]*)\>', line)
        positions.append([int(v.strip()) for v in values[0].split(",")])
        velocities.append([int(v.strip()) for v in values[1].split(",")])

    positions = np.array(positions)
    velocities = np.array(velocities)
    
    seconds = 0
    while seconds < 10391: 
        seconds += 1
        positions = apply_velocity(positions, velocities)
    plt.scatter(* positions.T)
    plt.gca().invert_yaxis()
    plt.show()


@np.vectorize
def apply_velocity(point, velocity):
    return point + velocity
    

if __name__ == "__main__":
    main()
