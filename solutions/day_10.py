from read import read_input
from functools import reduce


def save_signal():
    if cycle_counter in [20, 60, 100, 140, 180, 220]:
        signal_list.append((cycle_counter, x))


script_data = read_input('day_10.txt')
NOTHING_CMD = "noop"
ADD_CMD = "addx"
cycle_counter = 0
x = 1
signal_list = []

for instruction in script_data:
    cmd = instruction.split(" ")[0]
    if cmd == NOTHING_CMD:
        cycle_counter += 1
        save_signal()
    elif cmd == ADD_CMD:
        cycle_counter += 1
        save_signal()
        cycle_counter += 1
        save_signal()
        value = int(instruction.split(" ")[1])
        x += value

print(signal_list)
print(reduce(lambda partial_result, signal: partial_result + signal[0] * signal[1], signal_list, 0))


def print_pixel():
    if cycle_counter in sprite_position:
        print('#', end='')
    else:
        print('.', end='')


# part 2
sprite_position = [0, 1, 2]
middle_of_sprite = 1
cycle_counter = 0

for instruction in script_data:
    cmd = instruction.split(" ")[0]
    if cmd == NOTHING_CMD:
        print_pixel()
        if cycle_counter == 39:
            cycle_counter = -1
            print()
        cycle_counter += 1
    elif cmd == ADD_CMD:
        print_pixel()
        if cycle_counter == 39:
            cycle_counter = -1
            print()
        cycle_counter += 1
        print_pixel()
        if cycle_counter == 39:
            cycle_counter = -1
            print()
        cycle_counter += 1
        value = int(instruction.split(" ")[1])
        middle_of_sprite += value
        sprite_position = [middle_of_sprite - 1, middle_of_sprite, middle_of_sprite + 1]
