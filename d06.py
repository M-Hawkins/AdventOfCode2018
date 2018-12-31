# Advent of Code 2018 Day 6
# Matthew Hawkins


from collections import Counter
import numpy as np
from scipy.spatial import distance


def main():
    target_coordinates = np.loadtxt("input06.txt", delimiter=', ')
    xmin, ymin = target_coordinates.min(axis=0)
    xmax, ymax = target_coordinates.max(axis=0) + 1
    xvals = np.arange(xmin, xmax)
    yvals = np.arange(ymin, ymax)
    grid_coordinates = np.dstack(np.meshgrid(xvals, yvals)).reshape(-1, 2)
    distance_grid = distance.cdist(target_coordinates, grid_coordinates, metric='cityblock')

    # Part 1
    # Generate grid of closest target coordinates
    closest_target_grid = np.argmin(distance_grid, axis=0)
    # Remove equidistant points
    min_distance_grid = np.min(distance_grid, axis=0)
    equidistant_points = (distance_grid == min_distance_grid).sum(axis=0) > 1
    closest_target_grid[equidistant_points] = -1
    closest_target_grid = [dist for dist in closest_target_grid if dist != -1]

    counts = Counter(closest_target_grid)
    largest_area = counts.most_common(1)[0][1]
    print(largest_area)

    # Part 2
    max_safe_distance = 10000
    print(np.sum(sum(distance_grid) < max_safe_distance))


if __name__ == "__main__":
    main()
