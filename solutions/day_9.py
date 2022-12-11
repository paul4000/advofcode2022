from read import read_input

move_data = read_input('day_9.txt')

moves = [move.split(" ") for move in move_data]


# part 1
# (x,y) coordinates of H and T
def does_tail_touch_head(tail_coo, head_coo):
    T_x = tail_coo[0]
    T_y = tail_coo[1]
    H_x = head_coo[0]
    H_y = head_coo[1]
    x_distance = abs(T_x - H_x)
    y_distance = abs(T_y - H_y)
    return x_distance <= 1 and y_distance <= 1


def compute_tail_position_move_right(T_x, T_y, H_x, H_y):
    new_T_position = []
    if T_y == H_y:
        # -1 or 1
        new_T_position.append(T_x + 1)
        new_T_position.append(T_y)
    else:
        # diagonal move
        new_T_position.append(T_x + 1)
        if T_y < H_y:
            new_T_position.append(T_y + 1)
        else:
            new_T_position.append(T_y - 1)
    return new_T_position


def compute_tail_position_move_left(T_x, T_y, H_x, H_y):
    new_T_position = []
    new_T_position.append(T_x - 1)
    if T_y == H_y:
        # -1 or 1
        new_T_position.append(T_y)
    else:
        # diagonal move
        if T_y < H_y:
            new_T_position.append(T_y + 1)
        else:
            new_T_position.append(T_y - 1)
    return new_T_position


def compute_tail_position_move_up(T_x, T_y, H_x, H_y):
    new_T_position = []
    if T_x == H_x:
        # -1 or 1
        new_T_position.append(T_x)
    else:
        # diagonal move
        if T_x < H_x:
            new_T_position.append(T_x + 1)
        else:
            new_T_position.append(T_x - 1)
    new_T_position.append(T_y + 1)
    return new_T_position


def compute_tail_position_move_down(T_x, T_y, H_x, H_y):
    new_T_position = []
    if T_x == H_x:
        # -1 or 1
        new_T_position.append(T_x)
    else:
        # diagonal move
        if T_x < H_x:
            new_T_position.append(T_x + 1)
        else:
            new_T_position.append(T_x - 1)
    new_T_position.append(T_y - 1)
    return new_T_position


# initial position
H_position = [0, 0]
T_position = [0, 0]
T_positions = {(T_position[0], T_position[1])}

for move in moves:
    direction = move[0]
    steps_n = int(move[1])
    if direction == 'R':
        for i in range(0, steps_n):
            H_position[0] = H_position[0] + 1
            if not does_tail_touch_head(T_position, H_position):
                # compute tail position
                T_position = compute_tail_position_move_right(T_position[0],T_position[1], H_position[0], H_position[1])
                T_positions.add((T_position[0], T_position[1]))
    if direction == 'L':
        for i in range(0, steps_n):
            H_position[0] = H_position[0] - 1
            if not does_tail_touch_head(T_position, H_position):
                T_position = compute_tail_position_move_left(T_position[0],T_position[1], H_position[0], H_position[1])
                T_positions.add((T_position[0], T_position[1]))
    if direction == 'U':
        for i in range(0, steps_n):
            H_position[1] = H_position[1] + 1
            if not does_tail_touch_head(T_position, H_position):
                T_position = compute_tail_position_move_up(T_position[0],T_position[1], H_position[0], H_position[1])
                T_positions.add((T_position[0], T_position[1]))
    if direction == 'D':
        for i in range(0, steps_n):
            H_position[1] = H_position[1] - 1
            if not does_tail_touch_head(T_position, H_position):
                T_position = compute_tail_position_move_down(T_position[0],T_position[1], H_position[0], H_position[1])
                T_positions.add((T_position[0], T_position[1]))

# print(len(T_positions))

# part 2
knots_positions = [[0, 0] for i in range(0, 10)]
T_positions = {(0, 0)}

for move in moves:
    direction = move[0]
    steps_n = int(move[1])
    if direction == 'R':
        # move first head
        for i in range(0, steps_n):
            knots_positions[0][0] = knots_positions[0][0] + 1
            for i_of_knot, knot_current_head in enumerate(knots_positions[:-1]):
                current_tail = knots_positions[i_of_knot + 1]
                if not does_tail_touch_head(current_tail, knot_current_head):
                    knots_positions[i_of_knot + 1] = \
                        compute_tail_position_move_right(current_tail[0],current_tail[1], knot_current_head[0], knot_current_head[1])
            real_tail = knots_positions[-1]
            T_positions.add((real_tail[0], real_tail[1]))
    if direction == 'L':
        # move first head
        for i in range(0, steps_n):
            knots_positions[0][0] = knots_positions[0][0] - 1
            for i_of_knot, knot_current_head in enumerate(knots_positions[:-1]):
                current_tail = knots_positions[i_of_knot + 1]
                if not does_tail_touch_head(current_tail, knot_current_head):
                    knots_positions[i_of_knot + 1] = \
                        compute_tail_position_move_left(current_tail[0],current_tail[1], knot_current_head[0], knot_current_head[1])
            real_tail = knots_positions[-1]
            T_positions.add((real_tail[0], real_tail[1]))
    if direction == 'U':
        # move first head
        for i in range(0, steps_n):
            knots_positions[0][1] = knots_positions[0][1] + 1
            for i_of_knot, knot_current_head in enumerate(knots_positions[:-1]):
                current_tail = knots_positions[i_of_knot + 1]
                if not does_tail_touch_head(current_tail, knot_current_head):
                    knots_positions[i_of_knot + 1] = \
                        compute_tail_position_move_up(current_tail[0],current_tail[1], knot_current_head[0], knot_current_head[1])
            real_tail = knots_positions[-1]
            T_positions.add((real_tail[0], real_tail[1]))
    if direction == 'D':
        # move first head
        for i in range(0, steps_n):
            knots_positions[0][1] = knots_positions[0][1] - 1
            for i_of_knot, knot_current_head in enumerate(knots_positions[:-1]):
                current_tail = knots_positions[i_of_knot + 1]
                if not does_tail_touch_head(current_tail, knot_current_head):
                    knots_positions[i_of_knot + 1] = \
                        compute_tail_position_move_down(current_tail[0],current_tail[1], knot_current_head[0], knot_current_head[1])
            real_tail = knots_positions[-1]
            T_positions.add((real_tail[0], real_tail[1]))
    print(knots_positions)
    print("--------")

print(len(T_positions))



