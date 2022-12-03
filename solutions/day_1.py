from read import read_input

calories = read_input('day_1.txt')

# part 1
sum_calories = []
temp_sum = 0

for cal in calories:
    if cal == '':
        sum_calories.append(temp_sum)
        temp_sum = 0
    else:
        temp_sum += int(cal)

print(max(sum_calories))

# part 2
sum_calories.sort(reverse=True)
sum_of_three = sum_calories[0] + sum_calories[1] + sum_calories[2]
print(sum_of_three)