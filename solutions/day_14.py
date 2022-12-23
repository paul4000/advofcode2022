from read import read_input

data = read_input('day_14.txt')


def simulate_sand():
    sand_position = (500, 0)
    while True:
        # sand falls
        while True:
            down = (sand_position[0], sand_position[1] + 1)
            left_down = (sand_position[0] - 1, sand_position[1] + 1)
            right_down = (sand_position[0] + 1, sand_position[1] + 1)
            possible_new_position = list(
                filter(lambda sand_pos: sand_pos not in paths_points, [down, left_down, right_down]))
            if len(possible_new_position) == 0:
                break
            else:
                sand_position = possible_new_position.pop(0)
            # infinite falling
            if len(list(filter(lambda p: p[1] > sand_position[1], paths_points))) == 0:
                return
        paths_points.add(sand_position)
        sand_position = (500, 0)  # new sand grain


def simulate_sand_with_floor(floor_y):
    sand_position = (500, 0)
    while True:
        # sand falls
        while True:
            down = (sand_position[0], sand_position[1] + 1)
            left_down = (sand_position[0] - 1, sand_position[1] + 1)
            right_down = (sand_position[0] + 1, sand_position[1] + 1)
            possible_new_position = list(
                filter(lambda sand_pos: sand_pos not in paths_points and sand_pos[1] < floor_y, [down, left_down, right_down]))
            if len(possible_new_position) == 0:
                if sand_position == (500, 0):
                    paths_points.add(sand_position)
                    return
                break
            else:
                sand_position = possible_new_position.pop(0)
        paths_points.add(sand_position)
        sand_position = (500, 0)  # new sand grain


# part 1
# initialize 'matrix' of paths; list of stone's coordinates
paths_points = set()
for path in data:
    points = path.split(' -> ')
    for i, point in enumerate(points):
        # check if no last point, then end of path
        if i + 1 >= len(points):
            break
        first = point.split(',')
        first_point = (int(first[0]), int(first[1]))
        second = points[i + 1].split(',')
        second_point = (int(second[0]), int(second[1]))
        step_for_X = 1 if first_point[0] <= second_point[0] else -1
        step_for_Y = 1 if first_point[1] <= second_point[1] else -1
        for x in range(first_point[0], second_point[0] + step_for_X, step_for_X):
            for y in range(first_point[1], second_point[1] + step_for_Y, step_for_Y):
                paths_points.add((x, y))

# start pouring sand
number_of_path_points = len(paths_points)
# part 1
# simulate_sand()
floor_high = max([p[1] for p in paths_points]) + 2
# part 2
simulate_sand_with_floor(floor_high)

# how many new grains
print(len(paths_points) - number_of_path_points)