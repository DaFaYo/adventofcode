import time
import re
import math

start = time.time()

monkey_notes = {}
operators = ["*", "+", "-"]


def create_operation_function(argument, operator):
    if argument == "old":
        if operator == "*":
            return lambda x: x * x
        if operator == "+":
            return lambda x: 2 * x
        if operator == "-":
            return lambda x: 0
    else:
        argument = int(argument)
        if operator == "*":
            return lambda x: x * argument
        if operator == "+":
            return lambda x: x + argument
        if operator == "-":
            return lambda x: x - argument


def update_monkey_notes(monkey_note):
    monkey = int(re.findall(r'\d+', monkey_note[0])[0])
    starting_items = [int(item) for item in re.findall(r'\d+', monkey_note[1])]
    operation_list = monkey_note[2].split(" ")
    argument = ""
    operator = ""
    for i in range(len(operation_list)):
        if operation_list[i] in operators:
            operator = operation_list[i]
            argument = operation_list[i + 1]

    operation = create_operation_function(argument, operator)
    test = int(re.findall(r'\d+', monkey_note[3])[0])
    monkey_if_true = int(re.findall(r'\d+', monkey_note[4])[0])
    monkey_if_false = int(re.findall(r'\d+', monkey_note[5])[0])
    monkey_notes[monkey] = {
        "starting_items": starting_items,
        "operation": operation,
        "operator": operator,
        "test": test,
        "monkey_if_true": monkey_if_true,
        "monkey_if_false": monkey_if_false,
        "inspects_items": 0
    }


monkey_note = []
with open('test_input.txt', 'r') as f:
    for line in f:
        ln = line.strip()
        if ln:
            monkey_note.append(ln)
            if len(monkey_note) == 6:
                update_monkey_notes(monkey_note)
                monkey_note = []

end = time.time()

for dummy_index in range(20):
    for monkey, note in monkey_notes.items():
        while note["starting_items"]:
            item = note["starting_items"].pop(0)
            monkey_notes[monkey]["inspects_items"] += 1
            operation_func = note["operation"]
            worry_level = operation_func(item)
            worry_level = math.floor(worry_level / 3)
            if worry_level % note["test"] == 0:
                monkey_notes[note["monkey_if_true"]]["starting_items"].append(worry_level)
            else:
                monkey_notes[note["monkey_if_false"]]["starting_items"].append(worry_level)

for monkey, note in monkey_notes.items():
    print(f"Monkey {monkey}: {' '.join([str(x) for x in note['starting_items']])}")

print()

inspected_items_list = []
for monkey, note in monkey_notes.items():
    inspected_items = note['inspects_items']
    inspected_items_list.append(inspected_items)
    # print(f"Monkey {monkey} inspected items {inspected_items} times.")

inspected_items_list.sort(reverse=True)

print(f"The level of monkey business is {inspected_items_list[0] * inspected_items_list[1]}")
print(f"Process took: {round(end - start, 5)} seconds")
