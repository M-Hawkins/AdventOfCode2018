import numpy as np


def main():
    grid_serial = 9306
    grid_size = 300

    fuel_grid = []
    for x in range(1, grid_size):
        fuel_grid.append([calc_power_level(x, y, grid_serial) for y in range(1, grid_size)])
    fuel_grid = np.array(fuel_grid)
    fuel_grid = np.pad(fuel_grid, [1, 1], mode='constant')

    # Part 1
    p1_power, p1_coordinate = get_max(fuel_grid, grid_size, 3)
    print("{},{}".format(p1_coordinate[0], p1_coordinate[1]))

    # Part 2
    max_area = 1
    max_power, max_coordinate = get_max(fuel_grid, grid_size, max_area) 

    # Very slow, luckily the max power starts falling off quickly, so we stop early
    for area in range(max_area + 1, 20):
        power, coordinate = get_max(fuel_grid, grid_size, area)
        if power > max_power:
            max_power, max_coordinate, max_area = power, coordinate, area   

    print("{},{},{}".format(max_coordinate[0], max_coordinate[1], max_area))


def calc_power_level(x, y, grid_serial):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_serial
    power_level *= rack_id
    power_level = int("{:03.0f}".format(power_level)[-3])
    return power_level - 5


def get_max(grid, size, area):
    max_power = np.sum(grid[0:area, 0:area])
    max_coordinate = (0, 0)
    max_range = size - area - 1
    for x in range(max_range):
        for y in range(max_range):
            power = np.sum(grid[x:x+area, y:y+area])
            if power > max_power:
                max_power = power
                max_coordinate = (x, y)
    return max_power, max_coordinate


if __name__ == "__main__":
    main()
