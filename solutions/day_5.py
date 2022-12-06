from read import read_input
import re
import copy

instructions_data = read_input('day_5_instructions.txt')
number_pattern = re.compile('[0-9]+')
# 0 - how many crates, 1 - source stack, 2 - dest stack
instructions = [(int(number_instr[0]), int(number_instr[1]), int(number_instr[2])) for number_instr in
                (number_pattern.findall(instr) for instr in instructions_data)]
stacks_data = read_input('day_5_stacks.txt')[::-1]
stack_numbers = [int(st_num) for st_num in number_pattern.findall(stacks_data[0])]
# here I save stacks info
stacks_structure = dict()
for number in stack_numbers:
    stacks_structure[number] = []
letter_pattern = re.compile('\\[[A-Z]\\]')
for line_input in stacks_data[1:]:
    line_crates = line_input.split(' ')
    for i, crate in enumerate(line_crates):
        if letter_pattern.match(crate):
            stack = stacks_structure[i + 1]
            stack.append(crate)
stacks_structure_part2 = copy.deepcopy(stacks_structure)
# print(stacks_structure)

# part 1
for instruction in instructions:
    n_shifts = instruction[0]
    for i in range(0, n_shifts):
        src = instruction[1]
        dest = instruction[2]
        el = stacks_structure[src].pop()
        stacks_structure[dest].append(el)
print(stacks_structure)
# part 2
print(stacks_structure_part2)
for instruction in instructions:
    n_elements = instruction[0]
    src = instruction[1]
    dest = instruction[2]
    elements = stacks_structure_part2[src][-n_elements:]
    stacks_structure_part2[dest].extend(elements)
    stacks_structure_part2[src] = stacks_structure_part2[src][:-n_elements]
print(stacks_structure_part2)