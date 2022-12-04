from read import read_input

section_data = read_input('day_4.txt')

# part 1
formatted_sections = []

how_many_overlapped = 0
for pair_assignment_data in section_data:
    pair_assignment = pair_assignment_data.split(',')
    pair_1 = pair_assignment[0].split('-')
    pair_2 = pair_assignment[1].split('-')
    sections_1 = set(range(int(pair_1[0]), int(pair_1[1]) + 1))
    sections_2 = set(range(int(pair_2[0]), int(pair_2[1]) + 1))
    formatted_sections.append((sections_1, sections_2))

for sections_1, sections_2 in formatted_sections:
    how_many_overlapped += 1 if sections_1.issubset(sections_2) or sections_2.issubset(sections_1) else 0
print(how_many_overlapped)

# part 2
how_many_overlapped = 0

for sections_1, sections_2 in formatted_sections:
    how_many_overlapped += 1 if len(sections_1.intersection(sections_2)) > 0 else 0
print(how_many_overlapped)
