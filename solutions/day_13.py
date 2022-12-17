import ast
from read import read_input
from functools import cmp_to_key

data = read_input('day_13.txt')


def parse_input(input):
    chunk = []
    for line in input:
        if not line.strip():
            yield chunk
            chunk = []
        else:
            chunk.append(ast.literal_eval(line))
    yield chunk


def compare_list(l_element, r_element):
    if isinstance(l_element, int) and isinstance(r_element, int):
        # if left smaller than right then correct order
        if not l_element == r_element:
            return 1 if l_element < r_element else -1
        else:
            return 0
    if isinstance(l_element, list) and isinstance(r_element, int):
        return compare_list(l_element, [r_element])
    if isinstance(l_element, int) and isinstance(r_element, list):
        return compare_list([l_element], r_element)
    for r_inx, current_right in enumerate(r_element):
        if r_inx <= len(l_element) - 1:
            current_left = l_element[r_inx]
            comparison_result = compare_list(current_left, current_right)
            if not comparison_result == 0:
                return comparison_result
        else:
            # right is longer than left - right order
            return 1
    # if lengths are different it means that left element is longer - not right order
    return 0 if len(l_element) == len(r_element) else -1


# part 1
right_idx = []
for i, pair in enumerate(parse_input(data)):
    left = pair[0]
    right = pair[1]
    if compare_list(left, right) > 0:
        right_idx.append(i + 1)

# print(sum(right_idx))

# part 2
list_of_packets = []
for packets in parse_input(data):
    list_of_packets.extend(packets)
# dividers
div_1 = [[2]]
div_2 = [[6]]
list_of_packets.extend([div_1, div_2])
sorted_packets = sorted(list_of_packets, key=cmp_to_key(compare_list), reverse=True)
decoder_key = [i + 1 for i, el in enumerate(sorted_packets) if el == div_1 or el == div_2]
print(decoder_key[0] * decoder_key[1])