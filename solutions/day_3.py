from read import read_input
from string import ascii_lowercase as alc
from string import ascii_uppercase as auc

rucksacks_data = read_input('day_3.txt')

# part 1
# prepare points
points = {}
for i, letter in enumerate(alc):
    points[letter] = i + 1
for i, letter in enumerate(auc):
    points[letter] = i + 27

wrong_elements = []
for rucksack in rucksacks_data:
    first = rucksack[0:(len(rucksack)//2)]
    sec = rucksack[(len(rucksack)//2):]
    common_el = {*first}.intersection([*sec]).pop()
    wrong_elements.append(common_el)
s = sum([points[l] for l in wrong_elements])
print(s)

# part 2
badges = []
teams_3 = [rucksacks_data[i: i + 3] for i in range(0, len(rucksacks_data), 3)]
for team in teams_3:
    ruck_1 = team[0]
    ruck_2 = team[1]
    ruck_3 = team[2]
    common = {*ruck_1}.intersection([*ruck_2]).intersection([*ruck_3]).pop()
    badges.append(common)
s = sum([points[l] for l in badges])
print(s)