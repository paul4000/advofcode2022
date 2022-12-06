from read import read_input

input_sequence = read_input('day_6.txt')[0]

# part 1 & 2
L_OF_MARKER = 14
for inx, l in enumerate(input_sequence):
    if inx - L_OF_MARKER >= 0:
        potential_marker = input_sequence[inx - L_OF_MARKER:inx]
        if len(set(potential_marker)) == L_OF_MARKER:
            print(inx)
            break
