import time
import re
import math


def prime_factors(n):
    primes = {}

    while n % 2 == 0:
        if 2 in primes:
            primes[2] += 1
        else:
            primes[2] = 1
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            num = int(i)
            if num in primes:
                primes[num] += 1
            else:
                primes[num] = 1
            n = n / i

    if n > 2:
        primes[n] = 1

    return primes


def least_common_multiple(num_list):
    num_to_primes = {}
    set_of_primes = set()
    for num in num_list:
        if num not in num_to_primes:
            primes = prime_factors(num)
            for p in primes.keys():
                set_of_primes.add(p)

            num_to_primes[num] = primes

    _lcm = {}
    for _prime in set_of_primes:
        n = 1
        for primes in num_to_primes.values():
            if _prime in primes:
                if primes[_prime] > n:
                    n = primes[_prime]

        _lcm[_prime] = n

    return _lcm

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
        if operation_list[i] in ["*", "+", "-"]:
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

monkey_notes = {}
monkey_note = []
with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()
        if ln:
            monkey_note.append(ln)
            if len(monkey_note) == 6:
                update_monkey_notes(monkey_note)
                monkey_note = []

# compute least common multiple to use as modulo divisor
list_divisors = []
for note in monkey_notes.values():
    num = note["test"]
    if num not in list_divisors:
        list_divisors.append(num)

lcm = least_common_multiple(list_divisors)
divisor = 1
for prime, power in lcm.items():
    divisor *= (prime ** power)

index = 0
range_input = 10000

start = time.time()

for dummy_index in range(range_input):
    # index += 1
    # if index % 50 == 0:
    #     print(index)
    for monkey, note in monkey_notes.items():
        while note["starting_items"]:
            item = note["starting_items"].pop(0)
            monkey_notes[monkey]["inspects_items"] += 1
            operation_func = note["operation"]
            worry_level = operation_func(item)
            worry_level = worry_level % divisor
            if worry_level % note["test"] == 0:
                monkey_notes[note["monkey_if_true"]]["starting_items"].append(worry_level)
            else:
                monkey_notes[note["monkey_if_false"]]["starting_items"].append(worry_level)

end = time.time()

for monkey, note in monkey_notes.items():
    print(f"Monkey {monkey}: {' '.join([str(x) for x in note['starting_items']])}")

print()
inspected_items_list = []
for monkey, note in monkey_notes.items():
    inspected_items = note['inspects_items']
    inspected_items_list.append(inspected_items)
    print(f"Monkey {monkey} inspected items {inspected_items} times.")

inspected_items_list.sort(reverse=True)

print()
print(f"The level of monkey business is {inspected_items_list[0] * inspected_items_list[1]}")
print(f"Process took: {round(end - start, 5)} seconds")
