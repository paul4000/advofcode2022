import math


class Monkey:
    def __init__(self, number, items, operation, test, modulo):
        self.number = number
        self.items = items
        self.operation = operation
        self.test = test
        self.inspect_counter = 0
        self.modulo = modulo

    def inspect(self):
        self.inspect_counter += 1

    def clear_items(self):
        self.items = []

    def catch_item(self, item):
        self.items.append(item)

    def __str__(self):
        return "Monkey " + str(self.number) + " inspected items " + str(self.inspect_counter) + " times"


# init monkeys
# monkey_0 = Monkey(0, [89, 74], lambda x: x * 5, lambda x: 4 if x % 17 == 0 else 7, 17)
# monkey_1 = Monkey(1, [75, 69, 87, 57, 84, 90, 66, 50], lambda x: x + 3, lambda x: 3 if x % 7 == 0 else 2, 7)
# monkey_2 = Monkey(2, [55], lambda x: x + 7, lambda x: 0 if x % 13 == 0 else 7, 13)
# monkey_3 = Monkey(3, [69, 82, 69, 56, 68], lambda x: x + 5, lambda x: 0 if x % 2 == 0 else 2, 2)
# monkey_4 = Monkey(4, [72, 97, 50], lambda x: x + 2, lambda x: 6 if x % 19 == 0 else 5, 19)
# monkey_5 = Monkey(5, [90, 84, 56, 92, 91, 91], lambda x: x * 19, lambda x: 6 if x % 3 == 0 else 1, 3)
# monkey_6 = Monkey(6, [63, 93, 55, 53], lambda x: x * x, lambda x: 3 if x % 5 == 0 else 1, 5)
# monkey_7 = Monkey(7, [50, 61, 52, 58, 86, 68, 97], lambda x: x + 4, lambda x: 5 if x % 11 == 0 else 4, 11)
# test
monkey_0 = Monkey(0, [79, 98], lambda x: x * 19, lambda x: 2 if x % 23 == 0 else 3, 23)
monkey_1 = Monkey(1, [54, 65, 75, 74], lambda x: x + 6, lambda x: 2 if x % 19 == 0 else 0, 19)
monkey_2 = Monkey(2, [79, 60, 97], lambda x: x * x, lambda x: 1 if x % 13 == 0 else 3, 13)
monkey_3 = Monkey(3, [74], lambda x: x + 3, lambda x: 0 if x % 17 == 0 else 1, 17)

# monkeys = [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]
monkeys = [monkey_0, monkey_1, monkey_2, monkey_3]
for i in range(0, 20):
    for monkey in monkeys:
        for item in monkey.items:
            current_worry_level = monkey.operation(item)
            monkey.inspect()
            target_monkey_number = monkey.test(current_worry_level)
            final_worry_level = current_worry_level % monkeys[target_monkey_number].modulo
            monkeys[target_monkey_number].catch_item(final_worry_level if final_worry_level > 0 else current_worry_level)
        monkey.clear_items()

# which most active monkeys
sorted_monkeys = sorted(monkeys, reverse=True, key=lambda m: m.inspect_counter)
print(monkeys[0])
print(monkeys[1])
print(monkeys[2])
print(monkeys[3])
print(sorted_monkeys[0].inspect_counter * sorted_monkeys[1].inspect_counter)





